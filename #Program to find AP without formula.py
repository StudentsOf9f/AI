#Program to find AP without formula
a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))

ap_terms = []


for i in range(n):
    current_term = a + i * d 
    ap_terms.append(current_term) 


print("The Arithmetic Progression is:", ", ".join(map(str, ap_terms)))