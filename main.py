from application.input_handlers.argument_handler import ArgumentHandler
from application.commands.register_user_command import RegisterUserCommand
from application.commands.login_user_command import LoginUserCommand
from application.commands.create_task_command import CreateTaskCommand
from application.commands.list_tasks_command import ListTasksCommand
from application.commands.update_task_command import UpdateTaskCommand
from application.commands.delete_task_command import DeleteTaskCommand

def main():
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_arguments()

    if args.command == 'register':
        command = RegisterUserCommand(email=args.email, password=args.password)
    elif args.command == 'login':
        command = LoginUserCommand(email=args.email, password=args.password)
    elif args.command == 'create_task':
        command = CreateTaskCommand(title=args.title, description=args.description, user_email=args.user_email)
    elif args.command == 'list_tasks':
        command = ListTasksCommand(user_email=args.user_email)
    elif args.command == 'update_task':
        command = UpdateTaskCommand(task_id=args.task_id, title=args.title, description=args.description, user_email=args.user_email)
    elif args.command == 'delete_task':
        command = DeleteTaskCommand(task_id=args.task_id, user_email=args.user_email)
    else:
        print("Unknown command. Use -h for help.")
        return

    command.execute()

if __name__ == "__main__":
    main()
