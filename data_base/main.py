from data_base import db_connection
from data_base.models import Total_data
'''
def run():
    pass
'''

def crear_tablas():
    db_connection.Base.metadata.create_all(db_connection.get_engine())
    #run()
    print('Tablas creadas')

