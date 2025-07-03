from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from silabo.models import *
import random
import string

User = get_user_model()

class Command(BaseCommand):
    help = 'Genera datos de prueba masivos para el backend'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=50, help='Número de registros a generar')

    def handle(self, *args, **options):
        count = options['count']
        
        self.stdout.write(f"Generando {count} registros de prueba...")
        
        # Generar Universidades
        for i in range(min(count, 10)):
            universidad = Universidad.objects.create(
                nombre=f"Universidad Test {i+1}",
                codigo=f"UNI{i+1:03d}",
                direccion=f"Dirección {i+1}, Ciudad {i+1}",
                telefono=f"+51 9{random.randint(10000000, 99999999)}",
                email=f"contacto@uni{i+1}.edu.pe"
            )
            self.stdout.write(f"✅ Universidad creada: {universidad.nombre}")
        
        # Generar Facultades
        for i in range(min(count, 20)):
            universidad = random.choice(Universidad.objects.all())
            facultad = Facultad.objects.create(
                nombre=f"Facultad de {['Ingeniería', 'Medicina', 'Derecho', 'Economía', 'Educación'][i % 5]} {i+1}",
                codigo=f"FAC{i+1:03d}",
                universidad=universidad
            )
            self.stdout.write(f"✅ Facultad creada: {facultad.nombre}")
        
        # Generar Departamentos
        for i in range(min(count, 30)):
            facultad = random.choice(Facultad.objects.all())
            departamento = Departamento.objects.create(
                nombre=f"Departamento de {['Sistemas', 'Matemáticas', 'Física', 'Química', 'Biología'][i % 5]} {i+1}",
                codigo=f"DEP{i+1:03d}",
                facultad=facultad
            )
            self.stdout.write(f"✅ Departamento creado: {departamento.nombre}")
        
        # Generar Carreras
        for i in range(min(count, 25)):
            facultad = random.choice(Facultad.objects.all())
            carrera = Carrera.objects.create(
                nombre=f"Carrera de {['Ingeniería de Sistemas', 'Medicina Humana', 'Derecho', 'Economía', 'Educación'][i % 5]} {i+1}",
                codigo=f"CAR{i+1:03d}",
                facultad=facultad,
                duracion_anios=random.randint(4, 6)
            )
            self.stdout.write(f"✅ Carrera creada: {carrera.nombre}")
        
        # Generar Profesores
        for i in range(min(count, 40)):
            departamento = random.choice(Departamento.objects.all())
            profesor = Profesor.objects.create(
                nombres=f"Profesor {i+1}",
                apellidos=f"Apellido {i+1}",
                codigo=f"PROF{i+1:03d}",
                email=f"profesor{i+1}@universidad.edu.pe",
                telefono=f"+51 9{random.randint(10000000, 99999999)}",
                departamento=departamento
            )
            self.stdout.write(f"✅ Profesor creado: {profesor.nombres} {profesor.apellidos}")
        
        # Generar Cursos
        for i in range(min(count, 60)):
            carrera = random.choice(Carrera.objects.all())
            curso = Curso.objects.create(
                nombre=f"Curso de {['Programación', 'Matemáticas', 'Física', 'Química', 'Biología'][i % 5]} {i+1}",
                codigo=f"CUR{i+1:03d}",
                creditos=random.randint(2, 5),
                horas_teoricas=random.randint(2, 4),
                horas_practicas=random.randint(1, 3),
                carrera=carrera
            )
            self.stdout.write(f"✅ Curso creado: {curso.nombre}")
        
        # Generar Sílabos
        for i in range(min(count, 30)):
            curso = random.choice(Curso.objects.all())
            profesor = random.choice(Profesor.objects.all())
            silabo = Silabo.objects.create(
                titulo=f"Sílabo de {curso.nombre}",
                descripcion=f"Descripción del sílabo {i+1}",
                curso=curso,
                profesor=profesor,
                periodo_academico=f"2024-{random.randint(1, 2)}"
            )
            self.stdout.write(f"✅ Sílabo creado: {silabo.titulo}")
        
        self.stdout.write(self.style.SUCCESS(f"✅ Se generaron {count} registros de prueba exitosamente"))
