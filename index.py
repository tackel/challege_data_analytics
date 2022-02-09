from path_data.request import Archivos_request
from process_data.process_data import Process_data
'''
Archivos_request().request('museos')
Archivos_request().request('bibliotecas')
Archivos_request().request('cines')
'''

objeto_data = Process_data()
objeto_data.normalizar_data()
objeto_data.cantidades_conjuntas()
objeto_data.info_cines()
