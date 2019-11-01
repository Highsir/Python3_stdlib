import json

encoder = json.JSONEncoder()
data = [{'a':'A','b':(1,2),'c':3.0}]

for part in encoder.iterencode(data):
    print('PART:',part)