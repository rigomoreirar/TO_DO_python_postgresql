class User:
    def __init__(self, email: str, password_hash: str = None):
        self.email = email
        self.password_hash = password_hash
