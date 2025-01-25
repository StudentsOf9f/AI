#Program to find LCM of two numbers
def calculate_lcm(a, b):
    
    if a > b:
        greater = a
    else:
        greater = b

    while True:
      
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        else:
            greater += 1 

    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = calculate_lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {lcm}")
