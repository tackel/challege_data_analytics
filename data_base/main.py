from data_base import db_connection
from data_base.models import Total_data
import logging


def crear_tablas():
    try:
        db_connection.Base.metadata.create_all(db_connection.get_engine())
        logging.info('Tables were created')
        print('Tables were created')
    except (AttributeError) as e:
        logging.error(f'Error creating tables {e} ')
        print('Error creating tables ', e)
