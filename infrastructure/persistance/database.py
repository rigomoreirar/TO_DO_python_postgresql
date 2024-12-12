import psycopg2
from psycopg2.extras import RealDictCursor
from infrastructure.configuration.config import DATABASE_CONFIG

class Database:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = psycopg2.connect(
                host=DATABASE_CONFIG['host'],
                port=DATABASE_CONFIG['port'],
                dbname=DATABASE_CONFIG['dbname'],
                user=DATABASE_CONFIG['user'],
                password=DATABASE_CONFIG['password'],
                cursor_factory=RealDictCursor
            )
        return cls._connection
    
if __name__ == '__main__':
    connection = Database.get_connection()
    cursor = connection.cursor()
    cursor.close()
    connection.close()
