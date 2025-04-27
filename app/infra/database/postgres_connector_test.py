from unittest.mock import patch

import pytest

from infra.database.postgres_connector import PostgresConnector
from psycopg import AsyncConnection


@pytest.mark.asyncio
async def test_should_return_pool_on_success():

    pool: AsyncConnection = await PostgresConnector.get_connection()

    async with pool.connection() as con:
        await pool.check_connection(con)

def test_should_raise_error_if_connection_string_missing():
    with patch("infra.database.postgres_connector.getenv", return_value=None):
        with pytest.raises(ValueError, match="DATABASE_CONNECTION_STRING is not set"):
            PostgresConnector.init()
