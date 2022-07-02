from sgo_api.client.base import BaseClient
import config
import asyncio


URL = config.URL
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
SCHOOL_ID = config.SCHOOL_ID


async def main():
    async with BaseClient(url=URL) as client:
        await client.login(username=USERNAME, password=PASSWORD, school_id=SCHOOL_ID)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
