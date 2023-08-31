import os

# path = "C:/Users/timkr/PycharmProjects/pythonProject1/newFile"
# os.remove(path)

# f1 = open('myData', 'r')
# f2 = open('newFile', 'a')
#
# for data in f1:
#     f2.write(data)

f3 = open("Google.JPG","rb")
f4 = open("copy_Google.JPG","wb")
for data in f3:
    f4.write(data)