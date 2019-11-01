import asyncio

async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.5 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)

async def mian(num_phases):
    print('starting main')
    phases = [
        phase(i) for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    result = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {}'.format(answer))
        result.append(answer)
    print('result: {}'.format(result))
    return result

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(mian(3))
finally:event_loop.close()