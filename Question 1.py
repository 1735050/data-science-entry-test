def swap_values(x, y):
    """
    Task 1
    - Create a function that swaps the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric, and
    - Return swapped values if both x and y are numeric.
    """
    ## Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    ## Return -1 if either x or y is not numeric

    x, y = y, x
    ## Swap the values of x and y
    print(f"Swapped values: x = {x}, y = {y}")
    # Print the swapped values
    return x, y  # return swapped values



# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
# Get user input
try:
    # Get input from user and convert to float
    x = float(input("Enter first number (x): "))
    y = float(input("Enter second number (y): "))

    # Call the swap_values function
    result = swap_values(x, y)

    # If function returns swapped values
    if result != -1:
        x, y = result  # update x and y from returned swapped values
        print("Final values outside function:", x, y)
        # Print final result outside function

    else:
        print("Non-numeric values entered.")
        # Print error message if input was not numeric

except ValueError:
     # Handle error if input is not convertible to float
    print("Invalid input. Please enter numeric values.")
