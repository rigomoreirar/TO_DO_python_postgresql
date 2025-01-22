from .base_command import BaseCommand
from domain.services.task_service import TaskService
from infrastructure.adapters.task_repository_adapter import TaskRepositoryAdapter
from domain.exceptions.task_exceptions import TaskNotFoundException

class UpdateTaskCommand(BaseCommand):
    def __init__(self, task_id: int, title: str, description: str, user_email: str):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.user_email = user_email
        self.task_service = TaskService(task_repository=TaskRepositoryAdapter())

    def execute(self):
        try:
            self.task_service.update_task(self.task_id, self.title, self.description, self.user_email)
            print("Task updated successfully.")
        except TaskNotFoundException as e:
            print(str(e))
