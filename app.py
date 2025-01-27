import os
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test_db')
def test_db():
    try:
        # Connexion à la base de données MySQL
        connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'localhost'),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', 'mysecretpassword'),
            database=os.environ.get('MYSQL_DB', 'mydatabase')
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        cursor.close()
        connection.close()

        return f"Connected to database: {db_name}"

    except mysql.connector.Error as err:
        return f"Error: {err}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

