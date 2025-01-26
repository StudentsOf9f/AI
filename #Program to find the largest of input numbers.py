def largest_number():
    print("Enter the numbers one by one:")

    largest=None
    while True:
        user_input = input("Enter a number:")
        if user_input.lower()== 'done':
            break
        try:
            num=float(user_input)
            if largest is None or num>largest:
                largest=num
        except ValueError:
            print('Invalid Input! Please enter a number only!')

    if largest is not None:
        print("The largest number you entered is",largest,)
    else:
        print("No numbers were entered!")
largest_number()
