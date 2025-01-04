from domain.ports.task_repository_port import TaskRepositoryPort
from domain.models.task import Task
from infrastructure.persistence.database import Database
from typing import List

class TaskRepositoryAdapter(TaskRepositoryPort):
    def __init__(self):
        self.connection = Database.get_connection()

    def create_task(self, task: Task):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tasks (title, description, user_email) VALUES (%s, %s, %s) RETURNING id",
                (task.title, task.description, task.user_email)
            )
            task.id = cursor.fetchone()['id']
            self.connection.commit()

    def get_tasks_by_user(self, user_email: str) -> List[Task]:
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM tasks WHERE user_email = %s",
                (user_email,)
            )
            results = cursor.fetchall()
            tasks = []
            for row in results:
                tasks.append(Task(
                    id=row['id'],
                    title=row['title'],
                    description=row['description'],
                    user_email=row['user_email']
                ))
            return tasks

    def update_task(self, task: Task):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE tasks SET title = %s, description = %s WHERE id = %s AND user_email = %s",
                (task.title, task.description, task.id, task.user_email)
            )
            self.connection.commit()

    def delete_task(self, task_id: int):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM tasks WHERE id = %s",
                (task_id,)
            )
            self.connection.commit()
