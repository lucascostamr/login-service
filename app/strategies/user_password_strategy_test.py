from unittest.mock import AsyncMock

import pytest

from repository.user_repository import UserRepository
from strategies.user_password_strategy import UserPasswordStrategy

@pytest.mark.asyncio
async def test_should_return_user_data_on_success():
    user_repository = UserRepository()
    user_repository.get_user_data = AsyncMock(return_value={"user_data": "fake_data"})
    sut = UserPasswordStrategy(user_repository)

    response = await sut.authenticate("fake_username", "fake_password")

    assert response == {"user_data": "fake_data"}

@pytest.mark.asyncio
async def test_should_throw_on_user_not_found():
    user_repository = UserRepository()
    user_repository.get_user_data = AsyncMock(side_effect=Exception("User not found"))
    sut = UserPasswordStrategy(user_repository)

    with pytest.raises(Exception, match="User not found"):
        await sut.authenticate("fake_username", "fake_password")