from infrastructure.utilities.config_loader import ConfigLoader

config_loader = ConfigLoader()

DATABASE_CONFIG = {
    'host': config_loader.get('POSTGRESQL_DB_HOST'),
    'port': config_loader.get('POSTGRESQL_DB_PORT'),
    'dbname': config_loader.get('POSTGRESQL_DB_NAME'),
    'user': config_loader.get('POSTGRESQL_USERNAME'),
    'password': config_loader.get('POSTGRESQL_PASSWORD'),
}

if __name__ == '__main__':
    print(DATABASE_CONFIG)