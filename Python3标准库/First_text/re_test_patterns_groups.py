
import re

def text_patterns(text,patterns):
    for pattern,desc in patterns:
        print('{} {}\n'.format(pattern,desc))
        print('{}'.format(text))

        for match in re.finditer(pattern,text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print('{}{}{}'.format(prefix,text[s:e],' '*(len(text)-e)),end="")
            print(match.groups())

            if match.groupdict():
                print('{}{}'.format(' ' * (len(text)-s),match.groupdict()),)
        print()
    return

# if __name__ == '__main__':
#     text_patterns()