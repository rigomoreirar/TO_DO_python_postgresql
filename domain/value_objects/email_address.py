from infrastructure.utilities.validators import validate_email

class EmailAddress:
    def __init__(self, email: str):
        if not self._is_valid_email(email):
            raise ValueError(f"Invalid email address: {email}")
        self.email = email

    def _is_valid_email(self, email: str) -> bool:
        return validate_email(email) is not None

    def __str__(self):
        return self.email

    def __eq__(self, other):
        return self.email == other.email
