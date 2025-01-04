from abc import ABC, abstractmethod
from domain.models.user import User

class UserRepositoryPort(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass
