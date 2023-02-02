

from database.db import get_connection
from utils.DateFormat import DateFormat
from .entities.Usuario import Usuario


class UsuarioModel():

    @classmethod
    def login(self, user):
        try:
            connection=get_connection()
            eventos=[]
            with connection.cursor() as cursor:
                    sql = """SELECT idUsuario, correoUsuario, contrasenaUsuario, nombreUsuario FROM usuario 
                            WHERE correoUsuario = '{}'""".format(user.correoUsuario)
                    cursor.execute(sql)
                    print(sql)
                    row = cursor.fetchone()
                    if row != None:
                        print(row[0])
                        user = Usuario(row[0], row[1], Usuario.check_password(row[2], user.contrasenaUsuario), row[3])
                        print(user)
                        return user
                    else:
                        return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, id):
        try:
            connection=get_connection()
            eventos=[]
            with connection.cursor() as cursor:
                sql = """SELECT idUsuario, correoUsuario, nombreUsuario FROM usuario WHERE idUsuario = '{}'""".format(id)
                cursor.execute(sql)
                print(sql)
                row = cursor.fetchone()
                if row != None:
                    print(row[0])
                    return Usuario(row[0], row[1], None, row[2])
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)