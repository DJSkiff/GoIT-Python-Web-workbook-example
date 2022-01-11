'''https://goit.global/python-material-dev/docs/module-06/lesson-06-01#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-asyncio'''
import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']

async def call_url(url):
    print(f'Starting {url}')
    responce = await aiohttp.ClientSession().get(url)
    data = await responce.text()
    print(f'{url} bytes:{len(data)} {data[:200]}')
    return data


loop = asyncio.get_event_loop()

futures = [call_url(url) for url in urls]

results = loop.run_until_complete(asyncio.gather(*futures))

loop.close()