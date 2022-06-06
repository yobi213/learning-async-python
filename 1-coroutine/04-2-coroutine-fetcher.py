import aiohttp
import time
import asyncio
import ssl
import certifi


async def fetcher(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        "http://naver.com",
        "http://google.com",
        "http://instagrame.com",
    ] * 10

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=conn) as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())  # 4.335817813873291
    end = time.time()
    print(end - start)
