def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if input is a dictionary
    if not isinstance(dct, dict):
        raise ValueError("Input must be a dictionary")

    # If the key exists, print its original value
    if key in dct:
        print(f"Original value for '{key}':", dct[key])

    # Update or add the key-value pair
    dct[key] = value

    # Return the modified dictionary
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Test Case 1: Add a new key to an empty dictionary
dict1 = {}
result1 = update_dictionary(dict1, "name", "Alice")
print("Updated dictionary 1:", result1)
# Expected: {'name': 'Alice'}

# Test Case 2: Update existing key "age" from 25 to 26
dict2 = {"age": 25}
result2 = update_dictionary(dict2, "age", 26)
print("Updated dictionary 2:", result2)
# Expected Output:
# Original value for 'age': 25
# Updated dictionary 2: {'age': 26}
