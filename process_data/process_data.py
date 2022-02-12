import os
import pandas as pd
import glob
from datetime import datetime


today = datetime.now()
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
        
        print('3 data frame creados a partir de archivos csv')
    
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
        """ Concateno los 3 data frame"""
        self.total_data_frame = pd.concat([self.data1,self.data2,self.data3])

        """ Agrego la columna Fecha_Actualizacion en formato datetime """
        self.total_data_frame = self.total_data_frame.assign(Fecha_actualizacion=today)

        #self.total_data_frame.to_excel('total_data_frame.xlsx')
        print('Datos Para Tabla total_data Preparados')
        
        return self.total_data_frame
        
        
    def cantidades_conjuntas(self):
        """ Cantidad de registros totales por categoría """
        # Cambio el nombre a la columna para que no coincida con otra
        categoria_total = self.total_data_frame[['Categoria']].value_counts()
        categoria_total = categoria_total.reset_index(name='Cant_x_cat')
        categoria_total.rename(columns={
            'Categoria':'Categorias'
        }, inplace=True )
        
        
       
        """ Cantidad de registros totales por fuente """
        fuente_total = self.total_data_frame[['Fuente']].value_counts()
        fuente_total = fuente_total.reset_index(name='Cant_x_fuente')
       
        """ Cantidad de registros por provincia y categoría """
        prov_cat_total = self.total_data_frame[['Provincia','Categoria']].value_counts()
        prov_cat_total = prov_cat_total.reset_index(name='Cant_x_prov_cate')
        
        # concateno los df
        cant_data_final = pd.concat([categoria_total,fuente_total,prov_cat_total], axis=1)
        cant_data_final = cant_data_final.assign(Fecha_actualizacion=today)
        cant_data_final = cant_data_final.fillna('null')
      

        #cant_data_final.to_excel('data_final.xlsx')
        print('Datos Para Tabla Cantidades Preparados')
        
        return cant_data_final
        
    def info_cines(self):
        """ Funcion que arroja los datos para la tabla cines"""
        # Intercambio los si y null por 1 y 0
        mapear = {'si':1, 'null':0}
        self.data2['espacio_INCAA'] = self.data2['espacio_INCAA'].replace(mapear)
        
        # Sumo la cantidad de elementos para cada provincia
        cine_data = self.data2.groupby('Provincia')[['Pantallas','Butacas','espacio_INCAA']].sum()
        # Asigno la columna de fecha de actualizacion
        cine_data = cine_data.assign(Fecha_actualizacion=today)
        
        print('Datos Para Tabla Cine Preparados')
        
        return cine_data

obj = Process_data()
obj.normalizar_data()
obj.cantidades_conjuntas()
obj.info_cines()

