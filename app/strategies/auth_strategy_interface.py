from abc import ABC, abstractmethod

class AuthStrategy(ABC):

    @abstractmethod
    async def authenticate(self, **kwargs) -> dict:
        pass

    @abstractmethod
    def get_url_redirect(self) -> str:
        pass