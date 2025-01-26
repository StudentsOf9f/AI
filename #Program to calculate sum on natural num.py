#Program to calculate sum on natural numbers
def sum_natural_numbers():
    num=int(input("Enter a number:"))
    sum=num*(num+1)//2
    print(f"The sum of the natural numbers up to",num,"is:",sum)
sum_natural_numbers()