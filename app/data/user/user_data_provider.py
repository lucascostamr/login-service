from domain.user import User

class UserDataProvider:
    async def get_user_by_username(self, username: str) -> User:
        pass