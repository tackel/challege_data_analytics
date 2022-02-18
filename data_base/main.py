from data_base import db_connection
from data_base.models import Total_data
import logging

def crear_tablas():
    try:
        db_connection.Base.metadata.create_all(db_connection.get_engine())
        logging.info('Tablas Creadas')
        print('Tablas Creadas')
    except (AttributeError) as e:
        logging.error(f'Error al crear las tablas {e} ')
        print('Error al crear las tablas: ',e)

