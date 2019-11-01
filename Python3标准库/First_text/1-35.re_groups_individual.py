

import re

text = 'This is some test -- with punctuation'

regex = re.compile(r'(\bt\w+)\W+(\w+)')

print("pattern:",regex.pattern)

match = regex.search(text)
print('match:',match.group(0))
print('match:',match.group(1))
print('match:',match.group(2))
