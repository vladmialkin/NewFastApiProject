from envparse import Env

env = Env()


REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default='postgresql+asyncpg://login:password@localhost:5432/database'
)  # подключение к БД (асинхронное)
