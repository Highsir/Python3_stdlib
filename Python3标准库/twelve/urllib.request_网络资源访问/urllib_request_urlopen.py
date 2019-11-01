from urllib import request

response = request.urlopen('http://localhsot:8080/')
print('RESPONSE:',response)
print('URL     :',response.geturl())

headers = response.info()
print('DATE     :',headers['date'])
print('HEADEES  :')
print('---------')
print(headers)

data = response.read().decode('utf-8')
print('LENGTH   :',len(data))
print('DATA     :')
print('----------')
print(data)