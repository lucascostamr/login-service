from unittest.mock import MagicMock, AsyncMock

import pytest
from services.login_service import LoginService
from strategies.auth_strategy_interface import AuthStrategy


class FakeAuthStrategy(AuthStrategy):
    def get_url_redirect(self) -> str:
        return "url_redirect"

    async def authenticate(self) -> dict:
        return {"data": "fake_data"}


def make_sut(strategy_override: AuthStrategy = None) -> LoginService:
    strategy = strategy_override or FakeAuthStrategy()
    auth_strategies: dict[str, AuthStrategy] = {"fake_strategy": strategy}
    return LoginService(auth_strategies)


def test_should_return_redirect_url_on_success():
    sut = make_sut()
    response = sut.get_url_redirect("fake_strategy")

    assert response == "url_redirect"


def test_should_throw_error_if_strategy_not_found():
    sut = make_sut()
    with pytest.raises(ValueError):
        sut.get_url_redirect("wrong_strategy")


def test_should_throw_error_if_no_url_redirect_provided():
    fake_strategy = FakeAuthStrategy()
    fake_strategy.get_url_redirect = MagicMock(return_value=None)
    sut = make_sut(fake_strategy)

    with pytest.raises(ValueError):
        sut.get_url_redirect("fake_strategy")


@pytest.mark.asyncio
async def test_should_return_data_on_success():
    sut = make_sut()
    response = await sut.authenticate("fake_strategy")
    assert response == {"data": "fake_data"}


@pytest.mark.asyncio
async def test_should_throw_if_no_strategy_provided():
    sut = make_sut()
    with pytest.raises(ValueError):
        await sut.authenticate("wrong_strategy")


@pytest.mark.asyncio
async def test_should_throw_if_no_data_returned():
    fake_strategy = FakeAuthStrategy()
    fake_strategy.authenticate = AsyncMock(return_value=None)
    sut = make_sut(fake_strategy)

    with pytest.raises(ValueError):
        await sut.authenticate("fake_strategy")
