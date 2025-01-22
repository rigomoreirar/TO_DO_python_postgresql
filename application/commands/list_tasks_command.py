from .base_command import BaseCommand
from domain.services.task_service import TaskService
from infrastructure.adapters.task_repository_adapter import TaskRepositoryAdapter

class ListTasksCommand(BaseCommand):
    def __init__(self, user_email: str):
        self.user_email = user_email
        self.task_service = TaskService(task_repository=TaskRepositoryAdapter())

    def execute(self):
        tasks = self.task_service.list_tasks(self.user_email)
        if tasks:
            for task in tasks:
                print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")
        else:
            print("No tasks found.")
