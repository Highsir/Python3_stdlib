import json

from twelve.json_JavaScript对象记法 import json_myobj


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        print('default(', repr(o), ')')
        d = {
            '__class__': o.__class__.__name__,
            '__module__': o.__module__,
        }
        d.update(o.__dict__)
        return d

obj = json_myobj.MyObj('internal data')
print('obj: ',obj)
print()
print('myencoder: ',MyEncoder().encode(obj))
print()