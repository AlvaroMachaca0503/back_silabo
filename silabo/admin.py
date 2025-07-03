from django.contrib import admin
from .models import (
    Rol, CustomUser, Persona, LogProcesos, Profesion, Profesor, Estudiante,
    Universidad, Facultad, Departamento, Carrera, PlanCurricular, SemestreAcademico,
    SemestrePlan, PeriodoLectivo, Area, TipoCurso, Curso, CargaCurso, Grupo,
    Metodologia, Silabo, Unidad, Bibliografia, Semana, ContenidoEspecifico, Actividad, CriterioEvaluacion
)

admin.site.register(Rol)
admin.site.register(CustomUser)
admin.site.register(Persona)
admin.site.register(LogProcesos)
admin.site.register(Profesion)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Universidad)
admin.site.register(Facultad)
admin.site.register(Departamento)
admin.site.register(Carrera)
admin.site.register(PlanCurricular)
admin.site.register(SemestreAcademico)
admin.site.register(SemestrePlan)
admin.site.register(PeriodoLectivo)
admin.site.register(Area)
admin.site.register(TipoCurso)
admin.site.register(Curso)
admin.site.register(CargaCurso)
admin.site.register(Grupo)
admin.site.register(Metodologia)
admin.site.register(Silabo)
admin.site.register(Unidad)
admin.site.register(Bibliografia)
admin.site.register(Semana)
admin.site.register(ContenidoEspecifico)
admin.site.register(Actividad)
admin.site.register(CriterioEvaluacion)
