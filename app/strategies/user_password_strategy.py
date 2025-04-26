from domain.user import User
from infra.encrypters.encrypter import Encrypter
from infra.hashers.hasher import Hasher
from repository.user_repository import UserRepository
from strategies.auth_strategy_interface import AuthStrategy


class UserPasswordStrategy(AuthStrategy):
    def __init__(
        self, user_repository: UserRepository, hasher: Hasher, encrypter: Encrypter
    ):
        self.user_repository = user_repository
        self.hasher = hasher
        self.encrypter = encrypter

    async def authenticate(self, username: str, password: str) -> dict:
        user_data: User = await self.user_repository.get_user_by_username(username)
        is_valid_password = self.hasher.verify(password, user_data.password)
        if not is_valid_password:
            raise ValueError("Invalid credentials")

        token = self.encrypter.encrypt(user_data.user_id)

        return {
            "token": token,
            "user_data": {
                "username": user_data.username,
            },
        }

    def get_url_redirect(self) -> str:
        pass
