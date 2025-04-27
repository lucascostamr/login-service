import pytest
from unittest.mock import patch
from infra.hashers.bcrypt_adapter import BcryptAdapter


@patch("infra.hashers.bcrypt_adapter.checkpw")
def test_should_return_true_on_successful_hash(mock_checkpw):
    mock_checkpw.return_value = True

    bcrypt = BcryptAdapter()
    
    if bcrypt.verify("password", "hashed_password") is False:
        raise ValueError("Hash verification failed")

@patch("infra.hashers.bcrypt_adapter.checkpw")
def test_should_return_false_on_failed_hash(mock_checkpw):
    mock_checkpw.return_value = False

    bcrypt = BcryptAdapter()
    
    if bcrypt.verify("wrong_password", "hashed_password") is True:
        raise ValueError("Hash verification passed unexpectedly")

@patch("infra.hashers.bcrypt_adapter.checkpw")
def test_should_throw_if_checkpw_throws(mock_checkpw):
    mock_checkpw.side_effect = Exception("Error")

    bcrypt = BcryptAdapter()
    
    with pytest.raises(Exception, match="Error"):
        bcrypt.verify("password", "hashed_password")

@patch("infra.hashers.bcrypt_adapter.checkpw")
def test_should_call_checkpw_with_correct_params(mock_checkpw):
    bcrypt = BcryptAdapter()
    
    bcrypt.verify("password", "hashed_password")
    
    mock_checkpw.assert_called_once_with("password", "hashed_password")