import asyncio
import time

async def async_task(number, waiting):
    print(f"Process {number} started; take {waiting}s")
    await asyncio.sleep(waiting)
    print(f"Process {number} completed")

waiting = [1, 2, 3, 4, 5]

# Асинхронно
async def run_async():
    processes = [async_task(i, d) for i, d in enumerate(waiting)]
    await asyncio.gather(*processes)

start = time.time()
asyncio.run(run_async())
print(f"\nAsync execution took {time.time() - start:.2f} seconds\n")

# Последовательно
start = time.time()
for i, d in enumerate(waiting):
    print(f"Process {i} started; take {d}s")
    time.sleep(d)
    print(f"Process {i} completed")
print(f"\nSequential execution took {time.time() - start:.2f} seconds")
