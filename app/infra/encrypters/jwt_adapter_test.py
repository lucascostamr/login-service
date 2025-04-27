from unittest.mock import patch
from os import getenv

import pytest
from infra.encrypters.jwt_adapter import JwtAdapter


@patch("infra.encrypters.jwt_adapter.encode")
def test_should_return_token_on_success(mock_encode):
    mock_encode.return_value = "fake_token"

    sut = JwtAdapter()
    token = sut.encrypt({"fake_key": "fake_value"})

    if token != "fake_token":
        raise AssertionError("Expected 'fake_token', but got: " + token)

@patch("infra.encrypters.jwt_adapter.encode")
def test_should_throw_if_encode_throw(mock_encode):
    mock_encode.side_effect = Exception("fake_exception")

    sut = JwtAdapter()

    with pytest.raises(Exception, match="fake_exception"):
        sut.encrypt({"fake_key": "fake_value"})

@patch("infra.encrypters.jwt_adapter.encode")
def test_should_call_encode_with_correct_values(mock_encode):
    secret = getenv("JWT_SECRET")
    sut = JwtAdapter()
    sut.encrypt({"fake_key": "fake_value"})
    mock_encode.assert_called_once_with({"fake_key": "fake_value"}, secret, algorithm="HS256")