import pytest
from unittest.mock import AsyncMock
from repository.user_repository import UserRepository
from domain.user import User
from data.user.user_data_provider import UserDataProvider

@pytest.mark.asyncio
async def test_should_return_user_on_success():
    fake_user = User("fake_id", "fake_username", "fake_password")
    user_data_provider = UserDataProvider()
    user_data_provider.get_user_by_username = AsyncMock(return_value=fake_user)
    sut = UserRepository(user_data_provider)

    response = await sut.get_user_by_username("fake_username")

    if response != fake_user:
        raise AssertionError("Expected response to be equal to fake_user")