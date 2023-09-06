def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Example usage
number = 5  # Replace this with the desired number
factorial = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial}")
