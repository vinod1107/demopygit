from class_constructor_ import *
from types_of_class_methods import *


def main():
    # comp1 = Computer()
    # comp2 = Computer()
    # comp2.update()
    # print(comp1.compare_age(comp2))
    # print(Computer.state)
    s1 = Student(90, 95, 100)
    avg = s1.avg()
    print("average:", avg)
    school_name = Student.get_school()
    print("School Name:", school_name)
    Student.set_school('Akk')
    school_name = Student.get_school()
    print("School Name:", school_name)
    sum = Student.add(2, 5)
    print(sum)


if __name__ == "__main__":
    main()
