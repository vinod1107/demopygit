class Student:
    school = "Vageesha"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) // 3

    @classmethod
    def get_school(cls):
        return cls.school

    @classmethod
    def set_school(cls, name):
        cls.school = name

    @staticmethod
    def add(a, b):
        return a + b
