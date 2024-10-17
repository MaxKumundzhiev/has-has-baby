"""
Semaphore allows to limit amount of at the same time working threads.

Primer:
At the shop, there are 10 fitting rooms. U can not come into one of them until all of them are accupied.
Semaphore does the management distribution across fitting rooms, keeping track of who went out and who should come in.

The process of going in into fitting room is called - acquire
The process of going out of fitting room is called  - release

In asyncio, a Semaphore is a synchronization primitive 
that allows you to limit the number of simultaneous operations in a section of code.
"""

import asyncio

visitors = 0

async def fit_some_clothes(semaphore: asyncio.Semaphore):
    global visitors
    await semaphore.acquire()   # acquire fitting room, decrease fitting rooms
    await asyncio.sleep(2)      # fit
    visitors += 1
    print(f"it's ongoning fitting now, current visitors amount: {visitors}")
    semaphore.release()         # release fitting room, increase fitting rooms


async def main():
    semaphore = asyncio.Semaphore(value=10)  # value = 10 means 10 fitting rooms
    tasks = [asyncio.Task(fit_some_clothes(semaphore=semaphore)) for _ in range(100)]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())