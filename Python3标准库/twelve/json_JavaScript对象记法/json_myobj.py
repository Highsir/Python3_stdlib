class MyObj:
    def __init__(self,s):
        self.s = s

    def __enter__(self):
        return '<MyObj({})>'.format(self.s)

