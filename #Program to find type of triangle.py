#Program to find type of triangle
print("Input the sides of the triange as follows:")
a= int(input("Enter the first side of the triangle:"))
b= int(input("ENter the second side of the triangle:"))
c= int(input("Enter the third side of the triangle:"))
if a==b==c :
    print("It is an equilateral triangle:")
elif a==c or a==b or c==b:
    print("It is an isosceles triangle:")
else:
    print("It is a scalen triangle")

          