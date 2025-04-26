from unittest.mock import AsyncMock, MagicMock

import pytest
from data.user.user_data_provider import UserDataProvider
from domain.user import User
from repository.user_repository import UserRepository
from strategies.user_password_strategy import UserPasswordStrategy
from infra.hashers.hasher import Hasher

fake_user = User("fake_username", "fake_password")

@pytest.fixture
def hasher():
    return Hasher()

@pytest.fixture
def user_repository():
    return UserRepository(UserDataProvider())


@pytest.fixture
def sut(user_repository: UserRepository, hasher: Hasher):
    return UserPasswordStrategy(user_repository, hasher)


@pytest.mark.asyncio
async def test_should_return_token_on_success(
    user_repository: UserRepository, sut: UserPasswordStrategy
):
    user_repository.get_user_by_username = AsyncMock(value=fake_user)

    response = await sut.authenticate("fake_username", "fake_password")

    if response != "token":
        raise AssertionError(
            f"Expected {{'user_data': 'fake_data'}}, but got {response}"
        )


@pytest.mark.asyncio
async def test_should_throw_on_user_not_found(
    user_repository: UserRepository, sut: UserPasswordStrategy
):
    user_repository.get_user_by_username = AsyncMock(
        side_effect=Exception("User not found")
    )

    with pytest.raises(Exception, match="User not found"):
        await sut.authenticate("fake_username", "fake_password")


@pytest.mark.asyncio
async def test_should_call_get_user_by_username_with_correct_params(
    user_repository: UserRepository, sut: UserPasswordStrategy
):
    user_repository.get_user_by_username = AsyncMock(return_value=fake_user)

    await sut.authenticate("fake_username", "fake_password")

    user_repository.get_user_by_username.assert_awaited_once_with("fake_username")

@pytest.mark.asyncio
async def test_should_throw_on_invalid_password(sut: UserPasswordStrategy, hasher: Hasher, user_repository: UserRepository):
    user_repository.get_user_by_username = AsyncMock(return_value=fake_user)
    hasher.verify = MagicMock(return_value=False)

    with pytest.raises(ValueError, match="Invalid credentials"):
        await sut.authenticate("fake_username", "wrong_password")
