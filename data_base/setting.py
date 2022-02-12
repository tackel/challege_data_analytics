from decouple import config

DB_USER=config('DB_USER')
DB_PASSWORD= config('DB_PASSWORD')
DB_HOST= config('DB_HOST', default='localhost')
DB_PORT= config('DB_PORT', default=5432, cast=int)
DB_DATABASE= config('DB_DATABASE')
'''
DEBUG= config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG= config('TEMPLATE_DEBUG')
PERCENTILE= config('PERCENTILE')
'''