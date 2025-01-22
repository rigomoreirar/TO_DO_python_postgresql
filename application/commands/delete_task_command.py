from .base_command import BaseCommand
from domain.services.task_service import TaskService
from infrastructure.adapters.task_repository_adapter import TaskRepositoryAdapter
from domain.exceptions.task_exceptions import TaskNotFoundException

class DeleteTaskCommand(BaseCommand):
    def __init__(self, task_id: int, user_email: str):
        self.task_id = task_id
        self.user_email = user_email
        self.task_service = TaskService(task_repository=TaskRepositoryAdapter())

    def execute(self):
        try:
            self.task_service.delete_task(self.task_id, self.user_email)
            print("Task deleted successfully.")
        except TaskNotFoundException as e:
            print(str(e))
