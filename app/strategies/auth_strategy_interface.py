from abc import ABC, abstractmethod

class AuthStrategy(ABC):

    @abstractmethod
    async def authenticate(self, **kwargs):
        pass

    @abstractmethod
    def get_url_redirect(self):
        pass