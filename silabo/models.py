from django.db import models
from django.contrib.auth.models import User

# ─────────────────────────────────────────────
#  Estructura académica
# ─────────────────────────────────────────────
class Universidad(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100, blank=True)
    acronimo = models.CharField(max_length=50, blank=True)
    descripcion = models.TextField(blank=True)
    url = models.URLField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Facultad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.SET_NULL, null=True, related_name="facultades")
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    nombre = models.CharField(max_length=200)
    facultad = models.ForeignKey(Facultad, on_delete=models.SET_NULL, null=True, related_name="departamentos")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    nombre = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name="carreras")
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# ─────────────────────────────────────────────
#  Planes de estudio y periodos
# ─────────────────────────────────────────────
class PlanCurricular(models.Model):
    tag = models.CharField(max_length=255)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, related_name="planes")
    en_vigor = models.BooleanField(default=True)
    fecha_culminacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.carrera} - {self.tag}"


class SemestreAcademico(models.Model):
    nombre = models.CharField(max_length=255)
    anio_academico = models.PositiveSmallIntegerField()
    periodo = models.CharField(max_length=100)  # p.ej. 2025-I
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    semanas = models.PositiveSmallIntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.periodo})"


class SemestrePlan(models.Model):
    nombre = models.CharField(max_length=50)
    detalles = models.CharField(max_length=200)
    plan = models.ForeignKey(PlanCurricular, on_delete=models.SET_NULL, null=True, related_name="semestres")

    def __str__(self):
        return f"{self.plan} - {self.nombre}"


# ─────────────────────────────────────────────
#  Cursos y prerrequisitos
# ─────────────────────────────────────────────
class Area(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name="cursos")
    nombre = models.CharField(max_length=300)
    codigo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    horas_teoria = models.PositiveSmallIntegerField()
    horas_practica = models.PositiveSmallIntegerField()
    horas_laboratorio = models.PositiveSmallIntegerField()
    horas_teopra = models.PositiveSmallIntegerField(default=0)
    @property
    def horas_totales(self):
        return self.horas_teoria + self.horas_practica + self.horas_laboratorio + self.horas_teopra
    creditos = models.PositiveSmallIntegerField()
    semestre = models.ForeignKey(SemestrePlan, on_delete=models.SET_NULL, null=True, related_name="cursos")
    prerrequisitos = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="requeridos_por")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# ─────────────────────────────────────────────
#  Profesores y carga académica
# ─────────────────────────────────────────────
class Profesion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesor")
    profesion = models.ForeignKey(Profesion, on_delete=models.SET_NULL, null=True, blank=True)
    genero = models.CharField(max_length=1, choices=[("M", "Masculino"), ("F", "Femenino")])
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.usuario)


class CargaCurso(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="cargas")
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, related_name="cargas")
    detalles = models.CharField(max_length=100, blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.curso} - {self.profesor}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, related_name="grupos")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.curso})"


# ─────────────────────────────────────────────
#  Estudiantes
# ─────────────────────────────────────────────
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=[("M", "Masculino"), ("F", "Femenino")])
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombre}"


# ─────────────────────────────────────────────
#  Modelos complementarios para el sílabo y estructura académica extendida
# ─────────────────────────────────────────────

class Competencia(models.Model):
    descripcion = models.TextField()
    tipo = models.CharField(max_length=40, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion[:50]


class PerfilEgreso(models.Model):
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion[:50]


class Sumilla(models.Model):
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion[:50]


class Semana(models.Model):
    numero = models.PositiveSmallIntegerField()
    contenido = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Semana {self.numero}"


class Metodologia(models.Model):
    tipo = models.CharField(max_length=60)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo


class Bibliografia(models.Model):
    autor = models.CharField(max_length=120)
    libro = models.CharField(max_length=160)
    fecha = models.DateField()
    link = models.URLField(blank=True)
    nombre = models.CharField(max_length=160, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.libro


class Actividad(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class CriterioEvaluacion(models.Model):
    nombre = models.CharField(max_length=120)
    peso = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    inicio = models.DateField()
    final = models.DateField()
    descripcion = models.TextField()
    semana = models.ForeignKey(Semana, on_delete=models.SET_NULL, null=True, related_name="unidades")
    metodologia = models.ForeignKey(Metodologia, on_delete=models.SET_NULL, null=True, related_name="unidades")
    bibliografia = models.ForeignKey(Bibliografia, on_delete=models.SET_NULL, null=True, related_name="unidades")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion[:50]


# ─────────────────────────────────────────────
#  Silabos
# ─────────────────────────────────────────────

class Silabo(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="silabos")
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name="silabos")
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="silabos")
    periodo = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="silabos")
    campo_prueba = models.CharField(max_length=10, default='x')

    competencia = models.ForeignKey(Competencia, on_delete=models.SET_NULL, null=True, related_name="silabos")
    perfil = models.ForeignKey(PerfilEgreso, on_delete=models.SET_NULL, null=True, related_name="silabos")
    competencia_profesional = models.ForeignKey(
        Competencia, on_delete=models.SET_NULL, null=True, related_name="silabos_prof")
    sumilla = models.ForeignKey(Sumilla, on_delete=models.SET_NULL, null=True, related_name="silabos")
    unidad = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True, related_name="silabos")
    actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, null=True, related_name="silabos")
    criterio = models.ForeignKey(CriterioEvaluacion, on_delete=models.SET_NULL, null=True, related_name="silabos")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Silabo {self.periodo} - {self.curso}"
