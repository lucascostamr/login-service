from strategies.auth_strategy_interface import AuthStrategy

class LoginService:
    def __init__(self, auth_strategies: dict[str, AuthStrategy]):
        self.auth_strategies = auth_strategies

    def get_url_redirect(self, strategy: str) -> str:
        auth_strategy: AuthStrategy = self.auth_strategies.get(strategy)
        if auth_strategy is None:
            raise ValueError(f"Strategy {strategy} not found")
        url_redirect = auth_strategy.get_url_redirect()
        if url_redirect is None:
            raise ValueError("No url provided for redirection")
        return url_redirect

    async def authenticate(self, strategy: str, **kwargs) -> dict:
        auth_strategy: AuthStrategy = self.auth_strategies.get(strategy)
        if auth_strategy is None:
            raise ValueError(f"Strategy {strategy} not found")
        response = await auth_strategy.authenticate(**kwargs)
        if response is None:
            raise ValueError("No data provided")
        return response
