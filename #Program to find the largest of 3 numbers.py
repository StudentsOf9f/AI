#Program to find the largest of 3 numbers
def largest_of_three():
    num1 = float(input("Enter the first number:"))
    num2= float(input("Enter the second number"))
    num3= float(input("Enter the third number:"))
    largest = max(num1,num2,num3)
    print("The largest number is:",largest)

largest_of_three()
    