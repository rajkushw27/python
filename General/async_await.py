import asyncio


async def fetchData():
    print('staring fetching....')
    await asyncio.sleep(2)
    print('fetching done....')
    return {'data': 1}


async def printNumbers():
    for i in range(1, 10):
        print(i)
        await asyncio.sleep(0.30)
    print('done')


async def main():
    task1 = asyncio.create_task(fetchData())
    task2 = asyncio.create_task(printNumbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())
