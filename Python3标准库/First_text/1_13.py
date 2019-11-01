import textwrap
sample_text = '''I name is python.    I love candice.'''

def should_indent(line):
    print('indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0

dedented_text = textwrap.dedent(sample_text)

wrapped = textwrap.fill(dedented_text,width=50)
final = textwrap.indent(wrapped,'EVEN',predicate=should_indent)

print('\nQuoted block:\n')
print(final)
