import json

data = [{'a': 'A','b': (2,4),'c': 3.0}]
print('data:',data)

data_string = json.dumps(data)
print('encode:',data_string)

decodeed = json.loads(data_string)
print('decoded:',decodeed)

print('original:',type(data[0]['b']))
print('decoded:',type(decodeed[0]['b']))