from pytest import raises
from unittest.mock import MagicMock
from strategies.auth_strategy_interface import AuthStrategy
from services.login_service import LoginService


class FakeAuthStrategy(AuthStrategy):
    def get_url_redirect(self) -> str:
        return "url_redirect"

def make_sut(strategy_override: AuthStrategy = None) -> LoginService:
    strategy = strategy_override or FakeAuthStrategy()
    auth_strategies: dict[str, AuthStrategy] = {"fake_strategy": strategy}
    return LoginService(auth_strategies)

def test_should_return_redirect_url_on_success():
    sut = make_sut()
    response = sut.get_url_redirect("fake_strategy")

    assert response == "url_redirect"

def test_should_throw_error_if_no_url_redirect_provided():
    fake_strategy = FakeAuthStrategy()
    fake_strategy.get_url_redirect = MagicMock(return_value=None)
    sut = make_sut(fake_strategy)

    with raises(ValueError):
        sut.get_url_redirect("fake_strategy")
