def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Reverse the string using slicing
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Test Case 1: Reverse "Hello World"
result1 = string_reverse("Hello World")
print("Reversed 1:", result1)  # Expected: "dlroW olleH"

# Test Case 2: Reverse "Python"
result2 = string_reverse("Python")
print("Reversed 2:", result2)  # Expected: "nohtyP"