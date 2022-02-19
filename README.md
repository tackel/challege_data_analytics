Configuración:
Crear un entorno virtual.
Instalar las dependencias indicadas en le archivo requirements.txt
Configurar la conexión a la base de datos mediante un archivo .env (rellenar los datos correctos en el archivo existente)

Ejecución:
La ejecución de la aplicación se realiza mediante el archivo index.py
Los procesos son informados mediante logging en un archivo app.log y por consola.

Descripción:
La aplicación obtiene los datos de 3 archivos .csv que descarga y guarda en 3 carpetas diferentes. Las direcciones son creadas, si no existieran ya. Luego procesa esa información para poder guardarla.
Estos datos procesados se guardan en tres tablas distintas de acuerdo con las especificaciones dadas en el challenge. Las tablas fueron generadas utilizando el ORM SQLalchemy y la función de pandas dataframe.to_sql.
Si la base de datos no existe sera creada antes de generar las tablas.
