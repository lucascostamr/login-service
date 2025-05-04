from os import getenv

from psycopg import AsyncConnection
from psycopg_pool import AsyncConnectionPool


class PostgresConnector:
    pool: AsyncConnection | None = None

    @classmethod
    def init(cls):
        if cls.pool is None:
            connection_string = getenv("DATABASE_CONNECTION_STRING")

            if not connection_string:
                raise ValueError("DATABASE_CONNECTION_STRING is not set")

            cls.pool = AsyncConnectionPool(
                connection_string,
                open=False,
                min_size=1,
                max_size=10,
            )

    @staticmethod
    async def get_connection() -> AsyncConnection:
        if PostgresConnector.pool is None:
            PostgresConnector.init()

        await PostgresConnector.pool.open()

        return PostgresConnector.pool
