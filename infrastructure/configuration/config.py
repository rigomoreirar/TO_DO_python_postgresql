import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    'host': os.getenv('POSTGRESQL_DB_HOST'),
    'port': os.getenv('POSTGRESQL_DB_PORT'),
    'dbname': os.getenv('POSTGRESQL_DB_NAME'),
    'user': os.getenv('POSTGRESQL_USERNAME'),
    'password': os.getenv('POSTGRESQL_PASSWORD'),
}

if __name__ == '__main__':
    print(DATABASE_CONFIG)