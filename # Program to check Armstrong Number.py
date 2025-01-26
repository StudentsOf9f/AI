# Program to check Armstrong Number
def is_armstrong(n):
    digits = str(n)
    power= len(digits)
    return n == sum(int(digit)** power for digit in digits)

num = int(input("Enter a number"))
if is_armstrong(num):
    print(num,"is an Armstrong Number!")
else:
    print(num,"is not an Armstrong number!")