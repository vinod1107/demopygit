class PyCharm:

    def execute(self):
        print("compiling")
        print("running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("indentation")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = PyCharm()
me = MyEditor()
lap = Laptop()
lap.code(me)
