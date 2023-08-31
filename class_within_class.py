class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'i5'
            self.ram = '8GB'

        def show(self):
            return self.brand, self.cpu, self.ram


s = Student("Vinod", 25)
s.show()
# lap = s.Laptop()
b, c, r = s.lap.show()
print("Brand:", b, ',', "CPU:", c, ',', "RAM:", r)
