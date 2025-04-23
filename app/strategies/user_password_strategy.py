from strategies.auth_strategy_interface import AuthStrategy
from repository.user_repository import UserRepository


class UserPasswordStrategy(AuthStrategy):
    def __init__(
        self,
        user_repository: UserRepository
    ):
        self.user_repository = user_repository

    async def authenticate(self, username: str, password: str) -> dict:
        user_data: dict = await self.user_repository.get_user_data(username)
        return user_data
    
    def get_url_redirect(self) -> str:
        pass
