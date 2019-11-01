from urllib.parse import urlparse

url = 'https://www.zhipin.com/web/geek/resume?ka=header-resume'
parsed = urlparse(url)
print(parsed)