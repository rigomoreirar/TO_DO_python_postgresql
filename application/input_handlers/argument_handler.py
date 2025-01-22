import argparse

class ArgumentHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Task Manager Application")
        subparsers = self.parser.add_subparsers(dest='command')

        # Register command
        register_parser = subparsers.add_parser('register')
        register_parser.add_argument('email')
        register_parser.add_argument('password')

        # Login command
        login_parser = subparsers.add_parser('login')
        login_parser.add_argument('email')
        login_parser.add_argument('password')

        # Create task command
        create_task_parser = subparsers.add_parser('create_task')
        create_task_parser.add_argument('title')
        create_task_parser.add_argument('description')
        create_task_parser.add_argument('user_email')

        # List tasks command
        list_tasks_parser = subparsers.add_parser('list_tasks')
        list_tasks_parser.add_argument('user_email')

        # Update task command
        update_task_parser = subparsers.add_parser('update_task')
        update_task_parser.add_argument('task_id', type=int)
        update_task_parser.add_argument('title')
        update_task_parser.add_argument('description')
        update_task_parser.add_argument('user_email')

        # Delete task command
        delete_task_parser = subparsers.add_parser('delete_task')
        delete_task_parser.add_argument('task_id', type=int)
        delete_task_parser.add_argument('user_email')

    def parse_arguments(self):
        return self.parser.parse_args()
