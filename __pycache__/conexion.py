import pyodbc

def Conectar():
    try:
        Conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+'DESKTOP-LNQCV67\SQLEXPRESS'+';DATABASE='+'Base_saesige'+';UID='+'coordinador'+';PWD='+'12345')
        return Conexion

    except Exception as ex:
        print("Ocurrio un error", ex)
        return None
