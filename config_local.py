# Configuración para desarrollo local
import os

# Configuración de Django
os.environ.setdefault('DJANGO_SECRET_KEY', 'django-insecure-dev-key-for-local-development')
os.environ.setdefault('DJANGO_DEBUG', 'True')
os.environ.setdefault('ALLOWED_HOSTS', 'localhost,127.0.0.1')

# Configuración de base de datos PostgreSQL
os.environ.setdefault('DB_NAME', 'silabo_db')
os.environ.setdefault('DB_USER', 'postgres')
os.environ.setdefault('DB_PASSWORD', '123456789')
os.environ.setdefault('DB_HOST', 'localhost')
os.environ.setdefault('DB_PORT', '5432')

# Configuración de CORS para desarrollo
os.environ.setdefault('CORS_ALLOWED_ORIGINS', 'http://localhost:5173,http://127.0.0.1:5173')
