from conexion import *

def consulta(user,clave):
    coneccion = Conectar()
    if coneccion:
        with coneccion.cursor() as cursor:
            query = "SELECT * FROM USUARIO WHERE usuario = ? and clave = ?"
            cursor.execute(query, (user,clave,))
            resultado = cursor.fetchall()
            if resultado:
                for lista in resultado:
                    print(lista)
            else: 
                return None

