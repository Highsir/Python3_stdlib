from urllib import request
response = request.urlopen('http://localhost:8080/')
print(response)
for line in response:
    print(line.decode('utf-8').rstrip())