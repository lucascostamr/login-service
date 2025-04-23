from unittest.mock import AsyncMock

import pytest

from repository.user_repository import UserRepository
from strategies.user_password_strategy import UserPasswordStrategy

@pytest.mark.asyncio
async def test_should_return_user_data_on_success():
    user_repository = UserRepository()
    user_repository.get_user_data = AsyncMock(return_value={"username": "test_user"})
    sut = UserPasswordStrategy(user_repository)

    response = await sut.authenticate("test_user", "test_password")

    assert response == {"username": "test_user"}