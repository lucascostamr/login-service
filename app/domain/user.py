class User:
    def __init__(self, id: str, username: str, password: str):
        self.user_id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(username={self.username}, password={self.password})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username and self.password == other.password
