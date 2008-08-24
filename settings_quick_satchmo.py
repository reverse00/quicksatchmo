import os

PROJECT_NAME = 'quick_satchmo'
INSTALL_DIR = os.path.expanduser("~") # user directory, change to any directory you want

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = PROJECT_NAME             # Or path to database file if using sqlite3.
DATABASE_USER = 'vp'             # Not used with sqlite3.
DATABASE_PASSWORD = 'qwe123'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


# DO NOT change things below
qs_root = os.path.abspath(os.path.dirname(__file__))