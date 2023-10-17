from conexionbd import *

def consulta(usuario,clave):
    coneccion = Conectar()
    if coneccion:
        with coneccion.cursor() as cursor:
            query = "SELECT * FROM USUARIO WHERE usuario = ? and clave = ?"
            cursor.execute(query, (usuario,clave,))
            resultado = cursor.fetchall()
            if resultado:
                for lista in resultado:
                    return lista
            else:
                return None
    else:
        print("error en la consulta")

def insertar_usuario(usuario, clave):
    conexion = Conectar()
    if conexion:
        with conexion.cursor() as cursor:
            # Verifica si el usuario ya existe en la base de datos
            query = "SELECT usuario FROM USUARIO WHERE usuario = ?"
            cursor.execute(query, (usuario,))
            existing_user = cursor.fetchone()

            if existing_user:
                # El usuario ya existe, no lo insertes de nuevo
                return "El usuario ya existe."

            # Si el usuario no existe, procede con la inserción
            query = "INSERT INTO USUARIO (usuario, clave) VALUES (?, ?)"
            cursor.execute(query, (usuario, clave,))
            conexion.commit()
            return "Registro exitoso. Por favor, inicia sesión."
    else:
        print("Error al insertar usuario")
        return "Error al insertar usuario"
