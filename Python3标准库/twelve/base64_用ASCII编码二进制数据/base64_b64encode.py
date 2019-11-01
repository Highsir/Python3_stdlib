import base64
import textwrap

with open(__file__, 'r', encoding='utf-8') as input:
    raw = input.read()
    initial_data = raw.split('#end_pymotw_header')[1]

byte_string = initial_data.encode('utf-8')
print('byte_string:',byte_string)
print()
encode_data = base64.b64encode(byte_string)
print('encode_data:',encode_data)
print()

num_initail = len(byte_string)

padding = 3 - (num_initail % 3)

print('{} bytes before encodeing'.format(num_initail))
print('Expect {} padding bytes'.format(padding))
print('{} bytes after encodeing \n'.format(len(encode_data)))
print(encode_data)