a = 5
b = 0

try:
    print("resource open")
    # print(a/b)
    int(input("Enter a number:"))
except Exception as e:
    print("Exception raised:", e)
finally:
    print("resource closed")

print("Bye")