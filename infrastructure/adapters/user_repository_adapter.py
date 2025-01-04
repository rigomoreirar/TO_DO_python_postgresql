from domain.ports.user_repository_port import UserRepositoryPort
from domain.models.user import User
from infrastructure.persistence.database import Database

class UserRepositoryAdapter(UserRepositoryPort):
    def __init__(self):
        self.connection = Database.get_connection()

    def create_user(self, user: User):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (email, password_hash) VALUES (%s, %s)",
                (user.email, user.password_hash)
            )
            self.connection.commit()

    def find_by_email(self, email: str) -> User:
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE email = %s",
                (email,)
            )
            result = cursor.fetchone()
            if result:
                return User(
                    email=result['email'],
                    password_hash=result['password_hash']
                )
            return None
