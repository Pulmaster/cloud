from database.db import get_connection
from utils.DateFormat import DateFormat
from .entities.Evento import Evento


class EventoModel():

    @classmethod
    def get_eventos(self):
        try:
            connection=get_connection()
            eventos=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT idEvento, nombreEvento, fechaInicio, fechaFin, idUsuario FROM Evento ")
                resulset=cursor.fetchall()

                for row in resulset:
                    evento=Evento(row[0],row[1],row[2],row[3],row[4])
                    eventos.append(evento.to_JSON())
            connection.close()
            return eventos


        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def get_evento(self,idUsuario):
        try:
            connection=get_connection()
            eventos=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT idEvento, nombreEvento, fechaInicio, fechaFin, idUsuario FROM Evento where idUsuario = %s",(idUsuario,))
                resulset=cursor.fetchall()

                for row in resulset:
                    evento=Evento(row[0],row[1],row[2],row[3],row[4])
                    eventos.append(evento.to_JSON())
            connection.close()
            return eventos
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def update_evento(self,evento):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public.evento SET
                                nombreevento =%s, 
                                fechainicio =%s, 
                                fechafin = %s, 
                                idusuario = %s
                                 WHERE idevento = %s """,(evento.nombreEvento,evento.fechaInicio,evento.fechaFin,evento.idUsuario,evento.idEvento,))
                affected_rows=cursor.rowcount
                connection.commit() 
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_evento(self,evento):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.evento(
	                            idevento, nombreevento, fechainicio, fechafin, idusuario)
	                            VALUES (%s, %s, %s, %s, %s);""",(evento.idEvento,evento.nombreEvento,evento.fechaInicio,evento.fechaFin,evento.idUsuario))
                print(evento.idEvento)
                affected_rows=cursor.rowcount
                connection.commit() 
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def delete_evento(self,evento):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute(""" DELETE FROM public.evento WHERE idEvento = %s """,(evento.idEvento,))
                affected_rows=cursor.rowcount
                connection.commit() 
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    