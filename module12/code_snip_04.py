'''https://goit.global/python-material-dev/docs/module-12/lesson-12-01#%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D1%81%D0%BA%D0%B0%D1%8F-%D1%87%D0%B0%D1%81%D1%82%D1%8C'''
import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org', ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    '''For Windows environment uncomment next row'''
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())