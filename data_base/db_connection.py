from sqlalchemy import create_engine
#import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

from data_base import setting

#log = logging.getLogger(__name__)
def get_engine():
    try:
        url = f"postgresql://{setting.DB_USER}:{setting.DB_PASSWORD}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_DATABASE}"
        if not database_exists(url):
            create_database(url)
            print('Data Base no existe y fue creada')
            
        engine = create_engine(url)
        #log.info("engina creado!")
        print('Coneccion, engine, realizada con exito')
    except IOError:
        #log.exception("Failed to get database connection!")
        print("Failed to get database connection!")
        return None, 'fail'

    return engine
'''
def get_session():
    engine = get_engine()
    session = sessionmaker(bind=engine)()
    #session = Session()
    print('Session realizada con exito')
    return session
'''

#engine = get_engine()
#session = get_session()
Base = declarative_base()