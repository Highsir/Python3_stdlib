import json

decoder = json.JSONDecoder()

def get_decoded_and_remainder(input_data):
    obj, end = decoder.raw_decode(input_data)
    remaining = input_data[end:]
    return (obj, end, remaining)

encoded_object = '[{"a": "A", "c": 3.3, "b": [2,4]}]'
extra_text = 'This text is not JSON'

print('JSON first:')
data = ''.join([encoded_object, extra_text])
obj, end, remaining = get_decoded_and_remainder(data)

print('Object               :',obj)
print('End of parsed input  :',end)
print('Remianing text       :',repr(remaining))
print()

print('JSON embedded:')
try:
    data = ''.join([extra_text,encoded_object, extra_text])
    print('data:',data)
    obj, end, remianing = get_decoded_and_remainder(data)
except ValueError as err:
    print('ERROR:', err)