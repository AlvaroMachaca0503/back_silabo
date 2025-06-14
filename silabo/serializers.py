from rest_framework import serializers
from .models import *


# ─────────────────────────────────────────────
#  Estructura académica
# ─────────────────────────────────────────────
class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = "__all__"


class FacultadSerializer(serializers.ModelSerializer):
    universidad = serializers.StringRelatedField()   # o UniversidadSerializer(read_only=True)

    class Meta:
        model = Facultad
        fields = "__all__"


class DepartamentoSerializer(serializers.ModelSerializer):
    facultad = serializers.StringRelatedField()

    class Meta:
        model = Departamento
        fields = "__all__"


class CarreraSerializer(serializers.ModelSerializer):
    departamento = serializers.StringRelatedField()

    class Meta:
        model = Carrera
        fields = "__all__"


# ─────────────────────────────────────────────
#  Planes de estudio y periodos
# ─────────────────────────────────────────────
class PlanCurricularSerializer(serializers.ModelSerializer):
    carrera = serializers.StringRelatedField()

    class Meta:
        model = PlanCurricular
        fields = "__all__"


class SemestreAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemestreAcademico
        fields = "__all__"


class SemestrePlanSerializer(serializers.ModelSerializer):
    plan = serializers.StringRelatedField()

    class Meta:
        model = SemestrePlan
        fields = "__all__"


# ─────────────────────────────────────────────
#  Cursos y prerrequisitos
# ─────────────────────────────────────────────
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    area = serializers.StringRelatedField()
    semestre = serializers.StringRelatedField()
    prerrequisitos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Curso
        fields = "__all__"


# ─────────────────────────────────────────────
#  Profesores y carga académica
# ─────────────────────────────────────────────
class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = "__all__"


class ProfesorSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    profesion = serializers.StringRelatedField()

    class Meta:
        model = Profesor
        fields = "__all__"


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