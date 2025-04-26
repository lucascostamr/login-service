from strategies.auth_strategy_interface import AuthStrategy
from repository.user_repository import UserRepository
from domain.user import User
from infra.hashers.hasher import Hasher


class UserPasswordStrategy(AuthStrategy):
    def __init__(
        self,
        user_repository: UserRepository,
        hasher: Hasher
    ):
        self.user_repository = user_repository
        self.hasher = hasher

    async def authenticate(self, username: str, password: str):
        user_data: User = await self.user_repository.get_user_by_username(username)
        is_valid_password = self.hasher.verify(password, user_data.password)
        if not is_valid_password:
            raise ValueError("Invalid credentials")
        return "token"
    
    def get_url_redirect(self) -> str:
        pass
