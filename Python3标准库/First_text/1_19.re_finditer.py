
import re

text = 'abaaabaaaaabbbbbaaa'
pattern = 'ab'

for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print('found {} at {}:{}'.format(text[s:e],s,e))