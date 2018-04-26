import asyncio

async def speak_async():
    print('OMG asynchronicity!')

async def stop(loop):
    await(asyncio.sleep(50))
    loop.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(speak_async())
asyncio.Task(stop(loop))