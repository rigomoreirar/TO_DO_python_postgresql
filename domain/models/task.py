class Task:
    def __init__(self, id: int = None, title: str = '', description: str = '', user_email: str = ''):
        self.id = id
        self.title = title
        self.description = description
        self.user_email = user_email
