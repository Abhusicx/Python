import time
import asyncio

async def function1():
    time.sleep(3)
    print("func 1")

async def function2():
    time.sleep(3)
    print("func 2")

async def function3():
    time.sleep(3)
    print("func 3")

async def main():
    task = asyncio.create_task(function1)
    #await function1()
    await function2()
    await function3()

asyncio.run(main())