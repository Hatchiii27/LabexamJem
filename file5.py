def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print(f"Factorial of 5 is: {result}")

def sort_list(numbers):
    numbers.sort()
    return numbers

numbers = [5, 2, 8, 1, 3]
sorted_numbers = sort_list(numbers)
print(f"Sorted numbers: {sorted_numbers}")
