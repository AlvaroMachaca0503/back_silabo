import psycopg2

try:
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="testpass",
        host="localhost",
        port="5432"
    )
    print("¡Conexión exitosa!")
    conn.close()
except Exception as e:
    print("Error al conectar:", e) 