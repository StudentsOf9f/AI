# Program to find the largest of input numbers
def largest_number():
    print("Enter the numbers one by one")
    largest = None
    while True:
        try:
            user_input = input("Enter a number: ")
            print(f"DEBUG: Received input: {user_input}")  # Debug statement
            if user_input.lower() == 'done':
                break
            num = float(user_input)
            if largest is None or num > largest:
                largest = num
                print(f"DEBUG: New largest number: {largest}")  # Debug statement
        except ValueError:
            print("Invalid Input! Please enter a number only!")
    
    if largest is not None:
        print("The largest number you entered is", largest)
    else:
        print("No numbers were entered!")

largest_number()
