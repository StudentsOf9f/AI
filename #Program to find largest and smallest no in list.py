#Program to find largest and smallest no. in list
def find_largest_and_smallest(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest 

numbers = list(map(int, input("Enter numbers separated by spaces:").split()))
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number:",largest)
print(f"Smallest number:",smallest)
