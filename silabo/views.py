from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Actividad
from .serializers import ActividadSerializer
from .models import *
from .serializers import *


class UniversidadViewSet(viewsets.ModelViewSet):
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer


class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer


class PlanCurricularViewSet(viewsets.ModelViewSet):
    queryset = PlanCurricular.objects.all()
    serializer_class = PlanCurricularSerializer


class SemestreAcademicoViewSet(viewsets.ModelViewSet):
    queryset = SemestreAcademico.objects.all()
    serializer_class = SemestreAcademicoSerializer


class SemestrePlanViewSet(viewsets.ModelViewSet):
    queryset = SemestrePlan.objects.all()
    serializer_class = SemestrePlanSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para cursos:
    - GET    /cursos/          → lista
    - POST   /cursos/          → crear
    - GET    /cursos/{id}/     → detalle
    - PUT    /cursos/{id}/     → actualizar
    - PATCH  /cursos/{id}/     → actualización parcial
    - DELETE /cursos/{id}/     → eliminar
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ProfesionViewSet(viewsets.ModelViewSet):
    queryset = Profesion.objects.all()
    serializer_class = ProfesionSerializer


class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


class CargaCursoViewSet(viewsets.ModelViewSet):
    queryset = CargaCurso.objects.all()
    serializer_class = CargaCursoSerializer


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class CompetenciaViewSet(viewsets.ModelViewSet):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer


class PerfilEgresoViewSet(viewsets.ModelViewSet):
    queryset = PerfilEgreso.objects.all()
    serializer_class = PerfilEgresoSerializer


class SumillaViewSet(viewsets.ModelViewSet):
    queryset = Sumilla.objects.all()
    serializer_class = SumillaSerializer


class SemanaViewSet(viewsets.ModelViewSet):
    queryset = Semana.objects.all()
    serializer_class = SemanaSerializer


class MetodologiaViewSet(viewsets.ModelViewSet):
    queryset = Metodologia.objects.all()
    serializer_class = MetodologiaSerializer


class BibliografiaViewSet(viewsets.ModelViewSet):
    queryset = Bibliografia.objects.all()
    serializer_class = BibliografiaSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    
    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CriterioEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = CriterioEvaluacion.objects.all()
    serializer_class = CriterioEvaluacionSerializer


class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class SilaboViewSet(viewsets.ModelViewSet):
    queryset = Silabo.objects.all()
    serializer_class = SilaboSerializer
