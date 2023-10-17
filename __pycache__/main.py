from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from operaciones import *
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
        contra = request.form['password']
        logged = consulta(user, contra)
        if logged != None:
            usuario_logeado = user
            return redirect(url_for('home'))
        else:
            return render_template('Login-carwash.html')
    else:
        return render_template('Login-carwash.html')

@app.route('/home', methods = ['GET','POST'])
def home():





if __name__=='__main__':
#    app.config.from_object('')
    app.run(port=5000)