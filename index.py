from path_data.request import Archivos_request
from process_data.process_data import Process_data
from data_base.main import crear_tablas
from save_data.save_data import save
import logging



def main():
    """ Funcion init, ejecuta el programa en su totalidad"""
    # Configuracion logging
    logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('Comienza la ejecucion.')

    # Ejecucion descarga archivos csv 
    Archivos_request().request('museos')
    Archivos_request().request('bibliotecas')
    Archivos_request().request('cines')

    crear_tablas()
    #objeto_data = Process_data()
    #objeto_data.normalizar_data()
    #objeto_data.cantidades_conjuntas()
    #objeto_data.info_cines()
    save()
    logging.info('Finalizo la ejecucion.')


if __name__ == '__main__':
    main()



