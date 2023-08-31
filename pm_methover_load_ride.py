# method overloading

# class Add:
#     def sum(self, a, *b):
#         c = a
#         for i in b:
#             c = c + i
#         return c
#
#

# def sum(self, a=None, b=None, c=None):
#     if a != None and b != None and c != None:
#         s = a + b + c
#     elif a != None and b != None:
#         s = a + b
#     else:
#         s = a
#     return s


# a = Add()
# print(a.sum(5, 6))
class A:
    def show(self):
        print("A show")


class B(A):
    # pass
    def show(self):
        super().show()
        print("B Show")


b = B()
b.show()
