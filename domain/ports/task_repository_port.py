from abc import ABC, abstractmethod
from domain.models.task import Task
from typing import List

class TaskRepositoryPort(ABC):
    @abstractmethod
    def create_task(self, task: Task):
        pass

    @abstractmethod
    def get_tasks_by_user(self, user_email: str) -> List[Task]:
        pass

    @abstractmethod
    def update_task(self, task: Task):
        pass

    @abstractmethod
    def delete_task(self, task_id: int):
        pass
