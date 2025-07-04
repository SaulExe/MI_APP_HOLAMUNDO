from flask import Flask
import mysql.connector
import os
app = Flask(__name__)

@app.route('/')
def hello():
    # Conexión a la base de datos usando variables de entorno
    conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return f"Conectado a la base de datos: {db_name}"

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=5000)
