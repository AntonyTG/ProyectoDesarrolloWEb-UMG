from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import config
from operaciones import *
from cx_Oracle import *
from dotenv import load_dotenv
#from operaciones import insertar_usuario


#http://127.0.0.1:5000

app=Flask(__name__)
app.secret_key = 'your_secret_key' 

logged_user = None
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    global usuario_logeado
    global logged
    if request.method == 'POST':
        user = request.form['username']
        clave = request.form['password']
        validar = consulta(user,clave)
        
        if validar != None:
            return redirect(url_for('home'))
        else:
            return render_template('login.html')   
    else:
        return render_template('login.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    # Realiza una llamada a la API aquí y obtén los datos que necesitas
    api_url = 'http://127.0.0.1:5000'
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            # Procesa los datos de la API
            data = response.json()  #devuelve JSON      
            # Pasa los datos a tu plantilla para mostrarlos
            return render_template('menu.html', data=data)
        else:
            flash('Error al obtener datos de la API')
    except Exception as e:
        flash(f'Error: {str(e)}')
    
    return render_template('menu.html')

# Agrega una nueva ruta para el registro de usuarios
@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        # Accede a los campos del formulario correctamente usando los nombres correctos
        new_username = request.form['new_username']
        new_password = request.form['new_password']

        # Verifica si el usuario ya existe en la base de datos
        existing_user = consulta(new_username, new_password)

        if existing_user is None:
            # Inserta el nuevo usuario en la base de datos
            insertar_usuario(new_username, new_password)
            return jsonify('Registro exitoso. Por favor, inicia sesion'), 200
        else:
            return jsonify('El usuario ya existe. Intenta con otro nombre de usuario.'), 400

    return jsonify('Método no permitido'), 405

# Obtener todos los cursos
@app.route('/main/cursos', methods=['GET'])
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
@app.route('/main/estudiantes', methods=['GET'])
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
@app.route('/main/notas', methods=['GET'])
def get_notas():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM notas")
        notas = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(notas)

@app.route('/main/profesores', methods=['GET'])
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