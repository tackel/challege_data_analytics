from process_data.process_data import Process_data
import pandas as pd
from data_base.db_connection import get_engine
import logging


def save():
    """ Funcion que guarda los datos en la base de datos  """
    try:
        # Se genera la conexion
        con = get_engine()
        # Se obtine un objeto que procesa los datos
        obj = Process_data()

        obj.normalizar_data().to_sql('total_data', con=con,
                                     if_exists='replace', index_label='id')
        print('Data of Museos, Salas de Cine y Bibliotecas Populares stored in table total_data')
        logging.info(
            'Data of Museos, Salas de Cine y Bibliotecas Populares stored in table total_data')
        obj.cantidades_conjuntas().to_sql('registros_x_categoria',
                                          index_label='id', con=con, if_exists='replace')
        print('Data of Cantidades Conjuntas stored in table registros_x_categoria')
        logging.info(
            'Data of Cantidades Conjuntas stored in table registros_x_categoria')
        obj.info_cines().to_sql('cine_data', index_label='Provincia',
                                con=con, if_exists='replace')
        print('Data of Cine stored in table cine_data')
        logging.info('Data of Cine stored in table cine_data')
    except:
        logging.error('Failed to save data')
        print('Failed to save data')
