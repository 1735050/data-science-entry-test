def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both inputs are numeric (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both inputs must be numeric")   # If not, raise an error

    # Check if divisor is zero to prevent division by zero
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")

    # Return True if divisible, else False
    return num % divisor == 0       # if 0, it's divisible




# Test Case 1: Check if 10 is divisible by 2
result1 = check_divisibility(10, 2)
print("10 divisible by 2:", result1)  # Expected: True

# Test Case 2: Check if 7 is divisible by 3
result2 = check_divisibility(7, 3)
print("7 divisible by 3:", result2)  # Expected: False
