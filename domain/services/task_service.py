from domain.ports.task_repository_port import TaskRepositoryPort
from domain.models.task import Task
from typing import List
from domain.exceptions.task_exceptions import TaskNotFoundException, UnauthorizedAccessException

class TaskService:
    def __init__(self, task_repository: TaskRepositoryPort):
        self.task_repository = task_repository

    def create_task(self, title: str, description: str, user_email: str):
        task = Task(title=title, description=description, user_email=user_email)
        self.task_repository.create_task(task)

    def list_tasks(self, user_email: str) -> List[Task]:
        return self.task_repository.get_tasks_by_user(user_email)

    def update_task(self, task_id: int, title: str, description: str, user_email: str):
        tasks = self.task_repository.get_tasks_by_user(user_email)
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            raise TaskNotFoundException(f"Task with id {task_id} not found.")

        task.title = title
        task.description = description
        self.task_repository.update_task(task)

    def delete_task(self, task_id: int, user_email: str):
        tasks = self.task_repository.get_tasks_by_user(user_email)
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            raise TaskNotFoundException(f"Task with id {task_id} not found.")

        self.task_repository.delete_task(task_id)
