from strategies.auth_strategy_interface import AuthStrategy

class LoginService:
    def __init__(self, auth_strategies: dict[str, AuthStrategy]):
        self.auth_strategies = auth_strategies

    def get_url_redirect(self, strategy: str) -> str:
        auth_strategy: AuthStrategy = self.auth_strategies.get(strategy)
        url_redirect = auth_strategy.get_url_redirect()
        if url_redirect is None:
            raise ValueError("No url provided for redirection")
        return url_redirect