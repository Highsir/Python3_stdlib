import asyncio

async def consumer(condition, n):
    with await condition:
        print('consumer {} is waiting'.format(n))
        await condition.wait()
        print('consumer {} triggered'.format(n))
    print('ending consumer {}'.format(n))

async def mainpulate_condition(condition):
    print('starting mainpulate_condition')
    await asyncio.sleep(0.1)

    for i in range(1,3):
        with await condition:
            print('noifying remaining consumers')
            condition.notify(n=1)
        await asyncio.sleep(0.1)
    with await condition:
        print('notifying remaining consumers')
        condition.notify_all()

async def main(loop):
    condition = asyncio.Condition()
    consumers = [
        consumer(condition,i) for i in range(5)
    ]
    loop.create_task(mainpulate_condition(condition))
    await asyncio.wait(consumers)

et = asyncio.get_event_loop()
try:
    et.run_until_complete(main(et))
finally:
    et.close()