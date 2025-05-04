import pytest
from infra.database.postgres_connector import PostgresConnector
from psycopg import AsyncConnection


@pytest.mark.asyncio
async def test_should_return_pool_on_success():

    pool: AsyncConnection = await PostgresConnector.get_connection()

    async with pool.connection() as con:
        await pool.check_connection(con)
