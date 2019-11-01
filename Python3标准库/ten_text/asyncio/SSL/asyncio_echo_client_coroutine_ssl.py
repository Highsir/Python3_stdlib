import asyncio
import logging
import ssl
import sys

MESSAGE = [
    b'This is the message.',
    b'It will be sent ',
    b'in parts.',
]
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()

async def echo_client(address, messages):
    log = logging.getLogger('echo_client')
    log.debug('connection to {} port {}'.format(*address))

    # 增加ssl证书保证套接字客户端安全
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.check_hostname = False
    ssl_context.load_verify_locations('pymotw.crt')
    reader, writer = await asyncio.open_connection(*address, ssl=ssl_context)

    for msg in messages:
        writer.write(msg)
        log.debug('sending {!r}'.format(msg))
    writer.write(b'\x00')
    await writer.drain()

    log.debug('waiting for response')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('received {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return
try:
    event_loop.run_until_complete(
        echo_client(SERVER_ADDRESS, MESSAGE)
    )
finally:
    log.debug('closing even loop')
    event_loop.close()