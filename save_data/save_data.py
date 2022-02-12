from process_data.process_data import Process_data
import pandas as pd
from data_base.db_connection import get_engine

def save():
    """ Funcion que guarda los datos en la base de datos """
    con = get_engine()
    obj = Process_data()

    obj.normalizar_data().to_sql('total_data', con=con, if_exists='replace', index_label='id')
    print('Datos de Museos, Salas de Cine y Bibliotecas Populares Guardados en tabla total_data')
    
    obj.cantidades_conjuntas().to_sql('registros_x_categoria',index_label='id', con=con, if_exists='replace')
    print('Datos de Cantidades Conjuntas Guardados en la tabla registros_x_categoria')
   
    obj.info_cines().to_sql('cine_data',index_label='Provincia', con=con, if_exists='replace')
    print('Datos de Cine Guardados en la tabla cine_data')


