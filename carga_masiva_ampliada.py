from silabo.models import *
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

# Roles
rol_admin, _ = Rol.objects.get_or_create(nombre="Administrador")
rol_profesor, _ = Rol.objects.get_or_create(nombre="Profesor")
rol_estudiante, _ = Rol.objects.get_or_create(nombre="Estudiante")

# Universidad
uni, _ = Universidad.objects.get_or_create(
    nombre="Universidad Demo", direccion="Av. Principal 123", acronimo="UDEMO", descripcion="Universidad de prueba", url="http://udemo.edu", activo=True
)

# Facultades y Departamentos
facultades = []
departamentos = []
for i in range(1, 4):
    fac, _ = Facultad.objects.get_or_create(
        nombre=f"Facultad de Ingeniería {i}",
        descripcion=f"Facultad de Ingeniería número {i}",
        universidad=uni,
        activo=True
    )
    facultades.append(fac)
    for j in range(1, 3):
        dep, _ = Departamento.objects.get_or_create(
            nombre=f"Departamento {i}-{j}",
            facultad=fac,
            activo=True
        )
        departamentos.append(dep)

# Carreras
carreras = []
for idx, dep in enumerate(departamentos):
    for k in range(1, 3):
        car, _ = Carrera.objects.get_or_create(
            nombre=f"Carrera {idx+1}-{k}",
            departamento=dep,
            activo=True
        )
        carreras.append(car)

# Planes curriculares
planes = []
for idx, car in enumerate(carreras):
    for l in range(1, 3):
        plan, _ = PlanCurricular.objects.get_or_create(
            tag=f"Plan {idx+1}-{l}",
            carrera=car,
            activo=True
        )
        planes.append(plan)

# Semestres académicos
semestres_acad = []
for m in range(2023, 2026):
    for n in ["I", "II"]:
        sem_acad, _ = SemestreAcademico.objects.get_or_create(
            nombre=f"{m}-{n}",
            anio_academico=m,
            periodo=n,
            fecha_inicio=date(m, 3 if n == "I" else 8, 1),
            fecha_fin=date(m, 7 if n == "I" else 12, 31),
            semanas=20,
            descripcion=f"Semestre {m}-{n}"
        )
        semestres_acad.append(sem_acad)

# Semestres plan
semestres_plan = []
for idx, plan in enumerate(planes):
    for sidx, sem_acad in enumerate(semestres_acad[:2]):  # Solo 2 semestres por plan
        sem_plan, _ = SemestrePlan.objects.get_or_create(
            nombre=f"Semestre {sidx+1} del Plan {plan.tag}",
            detalles=f"Detalles del semestre {sidx+1} para el plan {plan.tag}",
            plan=plan,
            semestre_academico=sem_acad,
            activo=True
        )
        semestres_plan.append(sem_plan)

# Profesiones
profesiones = []
for i in range(1, 4):
    prof, _ = Profesion.objects.get_or_create(
        nombre=f"Profesión {i}",
        descripcion=f"Descripción de la profesión {i}",
        activo=True
    )
    profesiones.append(prof)

# Profesores y usuarios
profesores = []
for i in range(1, 6):
    user, _ = User.objects.get_or_create(
        email=f"profesor{i}@demo.com",
        defaults={
            "username": f"profesor{i}",
            "first_name": f"Profesor{i}",
            "last_name": f"Apellido{i}",
            "rol": rol_profesor,
            "is_superuser": False,
            "is_staff": True,
            "activo": True
        }
    )
    user.set_password(f"profesor{i}123")
    user.save()
    persona, _ = Persona.objects.get_or_create(
        nombre=f"Profesor{i}",
        apellido_paterno=f"Apellido{i}",
        apellido_materno=f"ApellidoM{i}",
        dni=f"{10000000+i}",
        fecha_nacimiento=date(1980+i, 1, 1),
        genero="M" if i % 2 == 0 else "F",
        nacionalidad="Peruana",
        telefono=f"99999{i}",
        usuario=user,
        activo=True
    )
    profesor, _ = Profesor.objects.get_or_create(
        persona=persona,
        profesion=profesiones[i % len(profesiones)],
        activo=True
    )
    profesores.append(profesor)

# Estudiantes y usuarios
estudiantes = []
for i in range(1, 11):
    user, _ = User.objects.get_or_create(
        email=f"estudiante{i}@demo.com",
        defaults={
            "username": f"estudiante{i}",
            "first_name": f"Estudiante{i}",
            "last_name": f"Apellido{i}",
            "rol": rol_estudiante,
            "is_superuser": False,
            "is_staff": False,
            "activo": True
        }
    )
    user.set_password(f"estudiante{i}123")
    user.save()
    persona, _ = Persona.objects.get_or_create(
        nombre=f"Estudiante{i}",
        apellido_paterno=f"Apellido{i}",
        apellido_materno=f"ApellidoM{i}",
        dni=f"{20000000+i}",
        fecha_nacimiento=date(2000+i, 5, 10),
        genero="F" if i % 2 == 0 else "M",
        nacionalidad="Peruana",
        telefono=f"98888{i}",
        usuario=user,
        activo=True
    )
    estudiante, _ = Estudiante.objects.get_or_create(
        persona=persona,
        activo=True
    )
    estudiantes.append(estudiante)

print("¡Carga masiva ampliada completada con éxito!")