from bcrypt import checkpw

from infra.hashers.hasher import Hasher

class BcryptAdapter(Hasher):
    def verify(self, value: str, hashed_value: str) -> bool:
        return checkpw(value, hashed_value)