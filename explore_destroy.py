class Foo(object):
    def __init__(self):
        print("Foo init running")

    def __del__(self):
        print("Destructor Foo")

class Bar(object):
    foo = Foo()
    def __init__(self):
        print("Bar init running")

    def __del__(self):
        print("Destructor Bar")

bar_obj = Bar()