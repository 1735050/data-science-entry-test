def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Start at the beginning of the list
    index = 0

    # Loop through the list using a while loop
    # The loop continues as long as index is less than the length of the list
    while index < len(lst):
        # Check if the current element is negative
        if lst[index] < 0:

            # If a negative number is found, return it immediately
            return lst[index]  # Return the first negative number found
        
        # Move to the next item in the list by increasing the index
        index += 1  

     # If no negative number was found in the loop, return this message
    return "No negatives"



# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]


# Test Case 1:A list that contains negative numbers
# The first negative number is -1 at index 2
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("First negative (Test Case 1):", result1)  # Expected: -1

# Test Case 2:A list that contains only non-negative numbers
# There is no negative number in the list
result2 = find_first_negative([2, 10, 7, 0])
print("First negative (Test Case 2):", result2)  # Expected: "No negatives"
