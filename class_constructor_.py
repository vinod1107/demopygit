class Computer:
    state = "Tamilnadu"

    def __init__(self):
        self.name = "Vinod"
        self.age = 43

    def update(self):
        self.age = 45

    def compare_age(self, other):
        if self.age == other.age:
            return True
        return False
