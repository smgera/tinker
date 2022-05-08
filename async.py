# based on https://realpython.com/async-io-python/
# Don’t get bogged down in generator-based coroutines, 
# which have been deliberately outdated by async/await. 

import asyncio
import time
import os
import writeFile

styles = [2,1,3,4] # norm, bold, ital, underline
clrANSI = '\033[0m'

async def coroutine(id):
    color = 1+id%8 # 1 to 8; 
    style = str(styles[id//8])
    ANSI ='\033[0;' + '38;5;' + str(color) + ';' + style + 'm' + f'{id:02}>'
    print(ANSI, 'calling sleep(1)' + clrANSI)
    writeFile.writeFile(writeFile.tempFilename(f'{id:02}_'),"")    
    await asyncio.sleep(1) # nonblocking call to another coroutine
    # await asyncio.sleep(1) # nonblocking call to another coroutine
    
    time.sleep(0.03)
    print(ANSI, 'done.' + clrANSI)

async def coordinator():
    await asyncio.gather(*(coroutine(i) for i in range(32)))

async def coordinator2():
    coroutine(2) # coroutines does not run if not awaited
    await coroutine(30) # coroutines does not run if not awaited
    # use tasks to start mulitple calls inside event loop
    taskC = asyncio.create_task(coroutine(0))
    task = asyncio.create_task(coroutine(1))
    await task # to wait for 1 task
    await asyncio.wait([task,taskC])


timeref = time.perf_counter()
if 0 :
    asyncio.run(coordinator())
else: 
    asyncio.get_event_loop().run_until_complete(coordinator2())
elapsed = time.perf_counter() - timeref
print(f'{elapsed:.2f}s')




