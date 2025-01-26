# Program to generate Fibonacci sequence up to 'n' terms

def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to n terms.
    """
    a, b = 0, 1  # First two terms of Fibonacci sequence
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence (1 term):")
        print(a)
    else:
        print(f"Fibonacci sequence ({n} terms):")
        print(a, b, end=" ")  # Print the first two terms
        for _ in range(2, n):  # Loop to calculate the next terms
            c = a + b
            print(c, end=" ")
            a, b = b, c  # Update the values for the next iteration
        print()  # Print a newline at the end

num_terms = int(input("Enter the number of terms: "))
generate_fibonacci(num_terms)

