from sqlalchemy import create_engine
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from data_base import setting


def get_engine():
    try:
        url = f"postgresql://{setting.DB_USER}:{setting.DB_PASSWORD}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_DATABASE}"
        if not database_exists(url):
            create_database(url)

            print('Data Base does not exist and was created')
            logging.info(
                f'Database does not exist and was created with the name {setting.DB_DATABASE} ')

        engine = create_engine(url)

        logging.info('Connection, engine, ok! ')
        print('Connection, engine, ok!')
        return engine

    except:
        logging.error("Failed to get database connection!")
        print("Failed to get database connection!")
        return None, 'fail'


'''
# Se crea la session para usar el orm
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
