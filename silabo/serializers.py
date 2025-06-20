from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# ─────────────────────────────────────────────
#  Estructura académica
# ─────────────────────────────────────────────

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Crea el usuario y le aplica set_password
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = "__all__"


class FacultadSerializer(serializers.ModelSerializer):
    universidad = serializers.PrimaryKeyRelatedField(queryset=Universidad.objects.all())
    universidad_detalle = UniversidadSerializer(source='universidad', read_only=True)

    class Meta:
        model = Facultad
        fields = ['id', 'nombre', 'descripcion', 'activa', 'universidad', 'universidad_detalle']


class DepartamentoSerializer(serializers.ModelSerializer):
    facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all())
    facultad_detalle = FacultadSerializer(source='facultad', read_only=True)

    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'activo', 'facultad', 'facultad_detalle']
        

class CarreraSerializer(serializers.ModelSerializer):
    departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())
    departamento_detalle = DepartamentoSerializer(source='departamento', read_only=True)

    class Meta:
        model = Carrera
        fields = ['id', 'nombre', 'activa', 'departamento', 'departamento_detalle']
        

# ─────────────────────────────────────────────
#  Planes de estudio y periodos
# ─────────────────────────────────────────────
class PlanCurricularSerializer(serializers.ModelSerializer):
    carrera = serializers.PrimaryKeyRelatedField(queryset=Carrera.objects.all())
    carrera_detalle = CarreraSerializer(source='carrera', read_only=True)

    class Meta:
        model = PlanCurricular
        fields = ['id', 'tag', 'en_vigor', 'fecha_culminacion', 'carrera', 'carrera_detalle']


class SemestreAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemestreAcademico
        fields = "__all__"


class SemestrePlanSerializer(serializers.ModelSerializer):
    plan = serializers.PrimaryKeyRelatedField(queryset=PlanCurricular.objects.all())
    plan_detalle = PlanCurricularSerializer(source='plan', read_only=True)


    class Meta:
        model = SemestrePlan
        fields = ['id', 'nombre', 'detalles', 'plan', 'plan_detalle']


# ─────────────────────────────────────────────
#  Cursos y prerrequisitos
# ─────────────────────────────────────────────
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    area_detalle = AreaSerializer(source='area', read_only=True)
    
    semestre = serializers.PrimaryKeyRelatedField(queryset=SemestrePlan.objects.all())
    semestre_detalle = SemestrePlanSerializer(source='semestre', read_only=True)
    
    prerrequisitos = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), many=True, write_only=True
    )
    prerrequisitos_detalle = serializers.StringRelatedField(
        many=True, source='prerrequisitos', read_only=True
    )

    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'codigo', 'descripcion', 'horas_teoria',
                  'horas_practica', 'horas_laboratorio', 'horas_teopra',
                  'creditos', 'activo', 'area', 'area_detalle',
                  'semestre', 'semestre_detalle',
                  'prerrequisitos', 'prerrequisitos_detalle']


# ─────────────────────────────────────────────
#  Profesores y carga académica
# ─────────────────────────────────────────────
class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = "__all__"


class ProfesorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    profesion = serializers.StringRelatedField(read_only=True)
    profesion_id = serializers.PrimaryKeyRelatedField(
        queryset=Profesion.objects.all(), write_only=True, source="profesion"
    )

    class Meta:
        model = Profesor
        fields = ["id", "usuario", "profesion", "profesion_id", "dni", "genero", "fecha_nacimiento", "nacionalidad", "telefono"]

    def create(self, validated_data):
        user_data = validated_data.pop("usuario")
        user = UserSerializer().create(user_data)
        profesor = Profesor.objects.create(usuario=user, **validated_data)
        return profesor



class CargaCursoSerializer(serializers.ModelSerializer):
    profesor = serializers.StringRelatedField()
    curso = serializers.StringRelatedField()

    class Meta:
        model = CargaCurso
        fields = "__all__"


class GrupoSerializer(serializers.ModelSerializer):
    curso = serializers.StringRelatedField()

    class Meta:
        model = Grupo
        fields = "__all__"


# ─────────────────────────────────────────────
#  Estudiantes
# ─────────────────────────────────────────────
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"


# ─────────────────────────────────────────────
#  Modelos de apoyo al sílabo
# ─────────────────────────────────────────────
class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = "__all__"


class PerfilEgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEgreso
        fields = "__all__"


class SumillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sumilla
        fields = "__all__"


class SemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semana
        fields = "__all__"


class MetodologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodologia
        fields = "__all__"


class BibliografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliografia
        fields = "__all__"


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"


class CriterioEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriterioEvaluacion
        fields = "__all__"


class UnidadSerializer(serializers.ModelSerializer):
    semana = serializers.StringRelatedField()
    metodologia = serializers.StringRelatedField()
    bibliografia = serializers.StringRelatedField()

    class Meta:
        model = Unidad
        fields = "__all__"


# ─────────────────────────────────────────────
#  Silabos
# ─────────────────────────────────────────────
class SilaboSerializer(serializers.ModelSerializer):
    profesor = serializers.StringRelatedField()
    facultad = serializers.StringRelatedField()
    carrera = serializers.StringRelatedField()
    curso = serializers.StringRelatedField()

    competencia = serializers.StringRelatedField()
    perfil = serializers.StringRelatedField()
    competencia_profesional = serializers.StringRelatedField()
    sumilla = serializers.StringRelatedField()
    unidad = serializers.StringRelatedField()
    actividad = serializers.StringRelatedField()
    criterio = serializers.StringRelatedField()

    class Meta:
        model = Silabo
        fields = "__all__"