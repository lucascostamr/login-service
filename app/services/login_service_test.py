from strategies.auth_strategy_interface import AuthStrategy

from services.login_service import LoginService


class FakeAuthStrategy(AuthStrategy):
    def get_url_redirect(self) -> str:
        return "url_redirect"


def test_should_return_redirect_url_on_success():
    auth_strategies: dict[str, AuthStrategy] = {"fake_strategy": FakeAuthStrategy()}
    sut = LoginService(auth_strategies)

    response = sut.get_url_redirect("fake_strategy")

    assert response == "url_redirect"
