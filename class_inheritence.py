class A:
    def __init__(self):
        print("class A init")

    def feature1(self):
        print("This is class A's feature 1 ")

    def feature2(self):
        print("This is class A's feature 2 ")


class B():

    def __init__(self):
        # super().__init__()
        print("class B init")

    def feature1(self):
        print("This is class B's feature 1 ")

    def feature4(self):
        print("This is class B's feature 4 ")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("class C init")

    def feature(self):
        super().feature1()



c = C()
print(c.feature1())
