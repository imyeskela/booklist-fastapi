from starlette.config import Config

config = Config('.env')

DB_URL = config('BL_DB_URL', cast=str, default='')