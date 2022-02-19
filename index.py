from path_data.request import Archivos_request
from process_data.process_data import Process_data
from data_base.main import crear_tablas
from save_data.save_data import save
import logging


def main():
    """ Funcion main, ejecuta el programa en su totalidad """
    # Configuracion logging
    try:
        logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG,
                            format='%(message)s %(asctime)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        logging.info('start of application')
        print('start of application')

        # Ejecucion descarga archivos csv
        Archivos_request().request('museos')
        Archivos_request().request('bibliotecas')
        Archivos_request().request('cines')
        # Ejecucion crear las 3 tablas
        crear_tablas()
        # Ejecucion procesa datos y guardar en tablas
        save()
        logging.info('End of application')
        print('End of application')
    except:
        logging.error('No se completo el proceso correctamente')
        print('No se completo el proceso correctamente')


if __name__ == '__main__':
    main()
