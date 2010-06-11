import os
ROOT_PATH = os.path.dirname(__file__)
# Make this unique, and don't share it with anybody.
SECRET_KEY = '**qe4h8e#8e^^5+ilz+=jj42x*fk3p87=ls1wnq--kpmg58e0^'

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(ROOT_PATH, 'db/bgcomm.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.