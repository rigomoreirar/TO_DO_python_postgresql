from domain.ports.user_repository_port import UserRepositoryPort
from domain.models.user import User
from infrastructure.services.password_hasher import PasswordHasher
from domain.exceptions.user_exceptions import UserAlreadyExistsException, InvalidCredentialsException, UserNotFoundException

class UserService:
    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def register_user(self, email: str, password: str):
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            raise UserAlreadyExistsException(f"User with email {email} already exists.")

        password_hash = PasswordHasher.hash_password(password)
        user = User(email=email, password_hash=password_hash)
        self.user_repository.create_user(user)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.find_by_email(email)
        if not user:
            raise UserNotFoundException(f"User with email {email} not found.")

        if not PasswordHasher.check_password(password, user.password_hash):
            raise InvalidCredentialsException("Invalid credentials.")
        return user
