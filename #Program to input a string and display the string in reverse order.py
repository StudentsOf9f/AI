# Program to input a string and display the string in reverse order
def reverse_string(s): 
    str1 = ""  
    for i in s:
        str1 = i + str1 
    return str1  

original_str = input("Enter the String please: ")

print("The original string is:", original_str)
print("The reverse string is:", reverse_string(original_str)) 
