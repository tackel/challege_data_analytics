import os
import pandas as pd
import glob
from datetime import datetime


class Process_data:
    def __init__(self):
        """ Se obtienen los path donde se encuentran los archivos csv y se generanlos data frame"""
        rutas = []
        content = []
        #data_frame = pd.DataFrame()

        for folder, subfolders, files in os.walk('path_data/'):  
            for file in files:  
                if file.endswith('.csv'):  

                    path = os.path.join(folder, file)
                    rutas.append(path)
                    
                    #df = pd.read_csv(path, index_col=None)
        
        self.data_frame_1 = pd.read_csv(rutas[0], index_col=None)
        self.data_frame_2 = pd.read_csv(rutas[1], index_col=None)
        self.data_frame_3 = pd.read_csv(rutas[2], index_col=None)
        self.total_data_frame = pd.DataFrame()
        '''
        data_frame_1.to_excel('data1.xlsx')
        data_frame_2.to_excel('data2.xlsx')
        data_frame_3.to_excel('data3.xlsx')
        '''
        print('3 data frame creados')
       

    def normalizar_data(self):
        
        """ Se Modifican los nombres de columnas para poder generar un data frame general,
        de bibliotecas, cines y museos"""
        
        self.data_frame_1.rename(columns={'Categoría':'Categoria',
                            'Cod_tel':'Cod_area',
                        'Teléfono': 'Telefono',
                        },
                inplace=True)
        self.data_frame_2.rename(columns={'Categoría':'Categoria',
                        'Dirección': 'Domicilio',
                        'cod_area':'Cod_area',
                        'Teléfono': 'Telefono',
                        'fuente':'Fuente',
                        },
                inplace=True)
        self.data_frame_3.rename(columns={'categoria':'Categoria',
                        'subcategoria':'Subcategoria',
                        'provincia': 'Provincia',
                        'localidad':'Localidad',
                        'nombre':'Nombre',
                        'direccion':'Domicilio',
                        'cod_area':'Cod_area',
                        'telefono': 'Telefono',
                        'fuente':'Fuente',
                        'piso':'Piso'
                        },
                inplace=True)
        """ Remplazar datos faltantes por null"""
        self.data1 = self.data_frame_1.fillna('null')
        self.data2 =self.data_frame_2.fillna('null')
        self.data3 = self.data_frame_3.fillna('null')

        """ Elimino columnas sobrantes """
        self.data1 = self.data1.drop(['Observacion','Departamento','Información adicional','Latitud','Longitud','TipoLatitudLongitud','Tipo_gestion','año_inicio','Año_actualizacion'],axis=1)
        self.data2 = self.data2.drop(['Observaciones','Departamento','Información adicional','Latitud','Longitud','TipoLatitudLongitud','tipo_gestion','año_actualizacion'],axis=1)
        self.data3 = self.data3.drop(['Observaciones','Info_adicional','Latitud','Longitud','TipoLatitudLongitud','jurisdiccion','año_inauguracion','IDSInCA'],axis=1)
        
        """ Modifico algunos datos que considoro erroneos"""
        self.data2['espacio_INCAA'] = self.data2['espacio_INCAA'].str.lower()
        self.data2.at[1,'espacio_INCAA']='null'
        

        self.data2.insert(4, "Subcategoria", 'null', allow_duplicates=False)
        self.data1.insert(15, "Pantallas", 'null', allow_duplicates=False)
        self.data1.insert(16, "Butacas", 'null', allow_duplicates=False)
        self.data1.insert(17, "espacio_INCAA", 'null', allow_duplicates=False)
        self.data3.insert(15, "Pantallas", 'null', allow_duplicates=False)
        self.data3.insert(16, "Butacas", 'null', allow_duplicates=False)
        self.data3.insert(17, "espacio_INCAA", 'null', allow_duplicates=False)
        '''
        self.data1.to_excel('data1.xlsx')
        self.data2.to_excel('data2.xlsx')
        self.data3.to_excel('data3.xlsx')
        '''
        self.total_data_frame = pd.concat([self.data1,self.data2,self.data3])
        """ Agrego la columna Fecha_Actualizacion en formato date() """
        today = datetime.now()

        self.total_data_frame.insert(19, 'Fecha_Actualizacion', today , allow_duplicates=False)
        self.total_data_frame['Fecha_Actualizacion'] = pd.to_datetime(self.total_data_frame['Fecha_Actualizacion'], format="%d/%m/%Y")
    

        #self.total_data_frame.to_excel('total_data_frame.xlsx')
        print('datas frames normalizados y concatenados en uno')
        
        
    def cantidades_conjuntas(self):
        
        """ Cantidad de registros totales por categoría """
        cat_total_registros = self.total_data_frame[['Categoria']].value_counts()
        print(cat_total_registros)

        """ Cantidad de registros totales por fuente """
        fuente_total_registro = self.total_data_frame[['Fuente']].value_counts()
        print(fuente_total_registro)

        """ Cantidad de registros por provincia y categoría """
        prov_cat_total = self.total_data_frame[['Provincia','Categoria']].value_counts()
        #prov_cat_total.to_excel('pct.xlsx')
        print(prov_cat_total)

        

    def info_cines(self):
        data_cine = self.data2[['Provincia','Pantallas','Butacas','espacio_INCAA']].value_counts()
        data_cine.to_excel('datos_cine.xlsx')
        print(data_cine)



