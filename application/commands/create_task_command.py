from .base_command import BaseCommand
from domain.services.task_service import TaskService
from infrastructure.adapters.task_repository_adapter import TaskRepositoryAdapter

class CreateTaskCommand(BaseCommand):
    def __init__(self, title: str, description: str, user_email: str):
        self.title = title
        self.description = description
        self.user_email = user_email
        self.task_service = TaskService(task_repository=TaskRepositoryAdapter())

    def execute(self):
        self.task_service.create_task(self.title, self.description, self.user_email)
        print("Task created successfully.")
