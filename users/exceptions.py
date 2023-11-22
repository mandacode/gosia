from gosia.exceptions import GosiaError


class UserAlreadyExists(GosiaError):
    message: str = "User already exists."
    name: str

    def __post_init__(self):
        username = "".join(self.name.split()).lower()
        self.message = f"User {self.name} ({username}) already exists."
