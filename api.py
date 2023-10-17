from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from operaciones import *
from dotenv import load_dotenv

app=Flask(__name__)


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
    return render_template('menu.html')

@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        # Accede a los campos del formulario correctamente usando los nombres correctos
        new_username = request.form['new_username']
        new_password = request.form['new_password']  # Debe coincidir con el nombre del campo en el formulario HTML

        # Verifica si el usuario ya existe en la base de datos
        existing_user = consulta(new_username, new_password)

        if existing_user is None:
            # Inserta el nuevo usuario en la base de datos
            insertar_usuario(new_username, new_password)
            flash('Registro exitoso. Por favor, inicia sesión.')
            return redirect(url_for('login'))
        else:
            flash('El usuario ya existe. Intenta con otro nombre de usuario.')

    return render_template('registro.html')



if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(port=5000)