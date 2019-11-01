import re

regexes = [re.compile(p) for p in ['this','that']]

text = "Does this text match the partten"

for regex in regexes:
    print('Seeking "{}" ->'.format(regex))

    if regex.search(text):
        print('match!')
    else:
        print('no match')