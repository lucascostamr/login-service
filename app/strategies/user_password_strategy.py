from strategies.auth_strategy_interface import AuthStrategy
from repository.user_repository import UserRepository
from domain.user import User


class UserPasswordStrategy(AuthStrategy):
    def __init__(
        self,
        user_repository: UserRepository
    ):
        self.user_repository = user_repository

    async def authenticate(self, username: str, password: str):
        user_data: User = await self.user_repository.get_user_by_username(username)
        return "token"
    
    def get_url_redirect(self) -> str:
        pass
