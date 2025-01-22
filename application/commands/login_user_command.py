from .base_command import BaseCommand
from domain.services.user_service import UserService
from infrastructure.adapters.user_repository_adapter import UserRepositoryAdapter
from domain.exceptions.user_exceptions import InvalidCredentialsException, UserNotFoundException

class LoginUserCommand(BaseCommand):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.user_service = UserService(user_repository=UserRepositoryAdapter())

    def execute(self):
        try:
            user = self.user_service.authenticate_user(self.email, self.password)
            print(f"User '{self.email}' logged in successfully.")
            # Store the user's session or token as needed
        except (InvalidCredentialsException, UserNotFoundException) as e:
            print(str(e))
