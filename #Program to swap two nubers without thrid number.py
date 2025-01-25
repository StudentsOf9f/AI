# Program to swap two numbers without a third variable
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Numbers before swapping: %d   %d\n" % (a, b))

a = a + b
b = a - b
a = a - b

print("Numbers after swapping are: %d   %d\n" % (a, b))
