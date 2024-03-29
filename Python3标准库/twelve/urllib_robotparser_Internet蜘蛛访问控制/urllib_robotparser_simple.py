from urllib import parse
from urllib import robotparser

AGENT_NAME = 'PyMOTW'
URL_BASE = 'https://pymotw.com/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()

PATHS = [
    '/',
    '/PyMOTW/',
    '/admin/',
    '/downloads/PyMOTW-1.92.tar.gz',
]

for path in PATHS:
    print('{} : {}'.format(parser.can_fetch(AGENT_NAME, path),path))
    url = parse.urljoin(URL_BASE, path)
    print('{} : {}'.format(parser.can_fetch(AGENT_NAME, url),url))
    print()