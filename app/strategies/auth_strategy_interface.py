from abc import ABC, abstractmethod

class AuthStrategy(ABC):

    @abstractmethod
    def get_url_redirect(self) -> str:
        pass