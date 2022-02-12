from data_base import db_connection
from sqlalchemy import Column, Integer, String, DateTime

""" Clase para generar las tablas"""
class Total_data(db_connection.Base):
    __tablename__ = 'total_data'
    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    Cod_Loc = Column(String)
    IdProvincia = Column(String)
    IdDepartamento = Column(String)
    Categoria = Column(String)
    Subcategoria = Column(String)
    Provincia = Column(String)
    Localidad = Column(String)
    Nombre = Column(String)
    Domicilio = Column(String)
    Piso = Column(String)
    CP = Column(String)
    Cod_area = Column(String)
    Telefono = Column(String)
    Mail = Column(String)
    Web = Column(String)
    Pantallas = Column(String)
    Butacas = Column(String)
    espacio_INCAA = Column(String)
    Fuente = Column(String)
    Fecha_actualizacion = Column(DateTime)
    
'''
    def __init__(self,id, Cod_Loc, IdProvincia,IdDepartamento,Categoria,Subcategoria,Provincia,Localidad,
    Nombre,Domicilio,Piso,CP,Cod_area,Telefono,Mail,Web,Pantallas,Butacas,espacio_INCAA,Fuente,Fecha_actualizacion):
        self.id = id
        self.Cod_Loc = Cod_Loc
        self.IdProvincia = IdProvincia
        self.IdDepartamento = IdDepartamento
        self.Categoria = Categoria
        self.Subcategoria = Subcategoria
        self.Provincia = Provincia
        self.Localidad = Localidad
        self.Nombre = Nombre
        self.Domicilio = Domicilio
        self.Piso = Piso
        self.CP = CP
        self.Cod_area =Cod_area
        self.Telefono = Telefono
        self.Mail = Mail
        self.Web = Web
        self.Pantallas = Pantallas
        self.Butacas = Butacas
        self.espacio_INCAA = espacio_INCAA
        self.Fuente = Fuente
        self.Fecha_actualizacion = Fecha_actualizacion

    def __repr__(self):
        return (f'Total_data({self.id},{self.Cod_Loc},{self.IdProvincia},{self.IdDepartamento},{self.Categoria},{self.Subcategoria},{self.Provincia},{self.Localidad},{self.Nombre},{self.Domicilio},{self.Piso},{self.CP},{self.Cod_area},{self.Telefono},{self.Mail},{self.Web},{self.Pantallas},{self.Butacas},{self.espacio_INCAA},{self.Fuente},{self.Fecha_actualizacion})')
    
    def __str__(self):
        return self.Categoria
'''