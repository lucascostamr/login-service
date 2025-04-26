from data.user.user_data_provider import UserDataProvider
from domain.user import User

class DbUser(UserDataProvider):
    async def get_user_by_username(self, username: str) -> User:
        pass