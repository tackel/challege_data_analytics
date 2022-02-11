from process_data.process_data import Process_data
import pandas as pd
from data_base.db_connection import get_engine

def save():
    objeto = Process_data() 
    objeto.normalizar_data().to_sql('total_data', con=get_engine(), if_exists='replace')
    print('Datos Guardados en tabla total_data')
    '''
    cant_conj = objeto.cantidades_conjuntas()
    for i in cant_conj:
        i.to_sql('cant_conjuntas', con=get_engine(), if_exists='append')
    print('Datos Guardados en tabla cant_conjuntas')
    '''
