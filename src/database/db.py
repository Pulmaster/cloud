import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host='100.25.117.21',
            user='ubuntu',
            password='ubuntu',
            database='NORCAL'



        )
    except DatabaseError as ex:
            raise ex