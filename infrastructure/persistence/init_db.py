from infrastructure.persistence.database import Database

def create_tables():
    connection = Database.get_connection()
    cursor = connection.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email VARCHAR(255) PRIMARY KEY,
            password_hash VARCHAR(255) NOT NULL
        );
    """)

    # Create tasks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            user_email VARCHAR(255) REFERENCES users(email)
        );
    """)

    connection.commit()
    cursor.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
