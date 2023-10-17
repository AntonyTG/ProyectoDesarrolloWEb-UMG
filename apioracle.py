from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
from cx_Oracle import *

# Crea una aplicación Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# Obtener todos los cursos
@app.route('/api/cursos', methods=['GET'])
def get_cursos():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cursos")
        cursos = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(cursos)

# Obtener todos los estudiantes
@app.route('/api/estudiantes', methods=['GET'])
def get_estudiantes():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        estudiantes = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(estudiantes)

# Puedes seguir el mismo patrón para otras tablas (notas, profesores, etc.)
@app.route('/api/notas', methods=['GET'])
def get_notas():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM notas")
        notas = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(notas)

@app.route('/api/profesores', methods=['GET'])
def get_profesores():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM profesores")
        profesores = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(profesores)

if __name__ == '__main__':
    app.run(debug=True)

