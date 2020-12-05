"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.
"""

def is_divisible(x, y):
    """ Check if x is divisible by y. Code obtained from section 6.4 of the textbook.
    """
    if x % y == 0:
        return True
    else:
        return False

def is_power(a, b):
    """ Check if a is a power of b
    """

    # Base cases
    if (a == b):
        # A number is a power of itself, thus a == b returns True
        return True
    elif b == 1:
        # If a != b and b == 1, a is not a power of 1, and it will go into an infinite loop if not break 
        return False

    # Core recursive logic to check if a is power of b
    if is_divisible(a, b):
        if is_power(a/b, b):
            return True
    return False


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))