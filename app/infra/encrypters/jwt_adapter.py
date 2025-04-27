from jwt import encode
from os import getenv

from infra.encrypters.encrypter import Encrypter

class JwtAdapter(Encrypter):
    def encrypt(self, data: dict) -> str:
        secret = getenv("JWT_SECRET")

        return encode(
            data,
            secret,
            algorithm="HS256",
        )