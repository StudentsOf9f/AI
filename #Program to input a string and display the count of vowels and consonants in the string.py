#Program to input a string and display the count of vowels and consonants in the string
str=input("Please enter a string as you wish:")
vowels = 0
consonants = 0
for i in str:
    if i in 'aeiouAEIOU':
        vowels += 1
    else:
        consonants += 1
print("The number of vowels:", vowels)
print("The number of consonants:", consonants)
