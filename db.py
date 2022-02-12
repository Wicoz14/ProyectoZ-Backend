import pymysql


def get_db():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='root', db='inst')
        return conexion
    except Error:
        print(Error)

def listar():
    conexion = get_db()
    j = []
    with conexion.cursor() as cursor:
        cursor.execute("SHOW TABLES FROM inst")
        j = cursor.fetchall()
    conexion.close()
    return j

