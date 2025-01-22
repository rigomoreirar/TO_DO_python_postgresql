from .base_command import BaseCommand
from domain.services.user_service import UserService
from infrastructure.adapters.user_repository_adapter import UserRepositoryAdapter
from domain.exceptions.user_exceptions import UserAlreadyExistsException

class RegisterUserCommand(BaseCommand):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.user_service = UserService(user_repository=UserRepositoryAdapter())

    def execute(self):
        try:
            self.user_service.register_user(self.email, self.password)
            print(f"User '{self.email}' registered successfully.")
        except UserAlreadyExistsException as e:
            print(str(e))
