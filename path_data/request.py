import requests
import pandas as pd
from pathlib import Path
from datetime import date
import os
import glob

class Archivos_request:
    def __init__(self):
        self.months = ("enero", "febrero", "marzo", "abri", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
        self.today = date.today()
        self.day = self.today.day
        self.month = self.today.month
        self.mes = self.months[self.today.month -1]
        self.year = self.today.year
    def request(self, categoria):
        if categoria == 'museos':
            url_museo = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv'
            req = requests.get(url_museo)
        elif categoria == 'cines':
            url_cines = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
            req = requests.get(url_cines)
        elif categoria == 'bibliotecas':
            url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
            req = requests.get(url_bibliotecas)


        if req: # elimina los achivos csv si es que hay un req para actualizarlos
            self.ruta = Path('path_data',f'{categoria}',f'{self.year}-{self.mes}')

            for folder, subfolders, files in os.walk(f'path_data/{categoria}'):  
                for file in files:  
                    if file.endswith('.csv'):  
                        path = os.path.join(folder, file)  
                        print('deleted : ', path ) 
                        os.remove(path)

            # creo la ruta
            self.ruta.mkdir(parents=True,exist_ok=True)
            # guardo el archivo en la ruta
            open(f'{self.ruta}/{categoria}-{self.day}-{self.month}-{self.year}.csv','wb').write(req.content)
            #datos = pd.read_csv(f'{ruta}/{categoria}-{self.day}-{self.month}-{self.year}.csv')
            
            print('Archivos guardado con exito')

            #print(datos.head())
            #print(r.status_code)
            #print(r.headers['content-type'])
            #print(r.encoding)
            #print(r.text)
            #print(r.json())
