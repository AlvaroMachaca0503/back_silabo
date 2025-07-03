#!/usr/bin/env python
"""
Script para crear un superusuario de prueba para el sistema de sílabos
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'silabo_s7_back.settings')
django.setup()

from django.contrib.auth import get_user_model
from silabo.models import Rol

User = get_user_model()

def create_superuser():
    """Crear un superusuario de prueba"""
    
    # Crear rol de administrador si no existe
    admin_rol, created = Rol.objects.get_or_create(
        nombre='Administrador',
        defaults={'activo': True}
    )
    
    if created:
        print(f"✅ Rol 'Administrador' creado")
    else:
        print(f"ℹ️  Rol 'Administrador' ya existe")
    
    # Crear superusuario
    try:
        user = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='admin123',
            is_staff=True,
            is_superuser=True,
            rol=admin_rol
        )
        print(f"✅ Superusuario creado exitosamente:")
        print(f"   Email: {user.email}")
        print(f"   Password: admin123")
        print(f"   Rol: {user.rol.nombre}")
        
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            print("ℹ️  El superusuario ya existe")
        else:
            print(f"❌ Error creando superusuario: {e}")

def create_test_user():
    """Crear un usuario de prueba normal"""
    
    # Crear rol de profesor si no existe
    profesor_rol, created = Rol.objects.get_or_create(
        nombre='Profesor',
        defaults={'activo': True}
    )
    
    if created:
        print(f"✅ Rol 'Profesor' creado")
    else:
        print(f"ℹ️  Rol 'Profesor' ya existe")
    
    # Crear usuario de prueba
    try:
        user = User.objects.create_user(
            username='profesor',
            email='profesor@example.com',
            password='profesor123',
            rol=profesor_rol
        )
        print(f"✅ Usuario de prueba creado exitosamente:")
        print(f"   Email: {user.email}")
        print(f"   Password: profesor123")
        print(f"   Rol: {user.rol.nombre}")
        
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            print("ℹ️  El usuario de prueba ya existe")
        else:
            print(f"❌ Error creando usuario de prueba: {e}")

if __name__ == '__main__':
    print("🚀 Creando usuarios de prueba...")
    print("-" * 50)
    
    create_superuser()
    print()
    create_test_user()
    
    print("-" * 50)
    print("✅ Proceso completado!")
    print("\n📝 Credenciales para probar:")
    print("   Admin: admin@example.com / admin123")
    print("   Profesor: profesor@example.com / profesor123") 