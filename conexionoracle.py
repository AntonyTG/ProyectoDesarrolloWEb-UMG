import cx_Oracle

def Conectar():
    try:
        conexion = cx_Oracle.connect(
            user='administrador',
            password='1234',
            dsn='localhost/XE',
            encoding='UTF-8'
        )
        return conexion

    except Exception as ex:
        print("Ocurrió un error:", ex)
        return None

def Consultar(conexion, sql):
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    except Exception as ex:
        print("Error al ejecutar la consulta:", ex)
        return None

conexion = Conectar()
if conexion:
    print("Conexión exitosa a Oracle")
    
    sql = "SELECT * FROM ESTUDIANTES"
    resultados = Consultar(conexion, sql)
    
    if resultados:
        for fila in resultados:
            print(fila)
    else:
        print("No se obtuvieron resultados")

    conexion.close()
else:
    print("No se pudo conectar a Oracle")
