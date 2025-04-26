from domain.user import User
from data.user.user_data_provider import UserDataProvider

class UserRepository:
    def __init__(self, user_data_provider: UserDataProvider):
        self.user_data_provider = user_data_provider

    async def get_user_by_username(self, username: str) -> User:
        user_data: User = await self.user_data_provider.get_user_by_username(username)
        return user_data
