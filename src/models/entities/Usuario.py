from utils.DateFormat import DateFormat
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):

  
    def __init__(self, idUsuario, correoUsuario=None, contrasenaUsuario=None, nombreUsuario=None)  -> None:
        self.idUsuario =  idUsuario
        self.nombreUsuario = nombreUsuario 
        self.correoUsuario = correoUsuario 
        self.contrasenaUsuario = contrasenaUsuario
    
    @classmethod
    def check_password(self, hashed_password, contrasenaUsuario):
        return check_password_hash(hashed_password, contrasenaUsuario)

  
    def to_JSON(self):
        return {
            'idUsuario' : self.idUsuario,  
            'nombreUsuario' : self.nombreUsuario, 
            'correoUsuario' : self.correoUsuario, 
            'contrasenaUsuario' : self.contrasenaUsuario,
            'idUsuario' : self.idUsuario 
            } 
    def get_id(self):
           return (self.idUsuario)

    