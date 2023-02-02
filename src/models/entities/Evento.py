from utils.DateFormat import DateFormat

class Evento():

  
    def __init__(self, idEvento, nombreEvento=None, fechaInicio=None, fechaFin=None, idUsuario=None)  -> None:
        self.idEvento =  idEvento
        self.nombreEvento = nombreEvento 
        self.fechaInicio = fechaInicio 
        self.fechaFin = fechaFin
        self.idUsuario = idUsuario
    
  
    def to_JSON(self):
        return {
            'idEvento' : self.idEvento,  
            'nombreEvento' : self.nombreEvento, 
            'fechaInicio' : DateFormat.convert_date (self.fechaInicio), 
            'fechaFin' : DateFormat.convert_date (self.fechaFin),
            'idUsuario' : self.idUsuario 
            } 