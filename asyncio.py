import asyncio
import time


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")


async def main():
    start = time.time()
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    end = time.time()
    print("Main Ended in .. ", end - start)


asyncio.run(main())