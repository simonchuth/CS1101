# Example 1
def sum_two_num(num_a, num_b):
    total = num_a + num_b
    print(total)

sum_two_num(2, 4)

"""
>>> sum_two_num(2, 4)
6

-`2` and `4` are the argument passed into the function `sum_two_num`. The parameters are `num_a` and `num_b`
"""

# Example 2
sum_two_num(2, 4)  # Values as arguments

a = 5
b = 10
sum_two_num(a, b)  # Variable as arguments

sum_two_num(3 + 5, 6 + b)  # Expression as arguments

"""
>>> sum_two_num(2, 4)
6

>>> a = 5
>>> b = 10
>>> sum_two_num(a, b)
15

>>> sum_two_num(3 + 5, 6 + b)
24
"""

# Example 3
def sum_two_num_local():
    num_a = 4
    num_b = 2

print(num_a)
"""
NameError: name 'num_a' is not defined

-`num_a` is a local variable defined within `sum_two_num_local`, hence it raise a NameError when used outside the function.
"""

# Example 4
def sum_two_num_parameter(num_a, num_b):
    total = num_a + num_b
    print(total)

print(num_a + num_b)
"""
NameError: name 'num_a' is not defined

-`num_a` and `num_b` are local variables within `sum_two_num_parameter`, hence it raise a NameError when used outside the function.
"""

# Example 5
num_x = 100  # Global
def sum_two_num_global_local_1():
    num_x = 10  # Local
    total = num_x + 2
    print(total)

sum_two_num_global_local_1()

num_y = 100  # Global
def sum_two_num_global_local_2():
    total = num_y + 2
    print(total)

sum_two_num_global_local_2()

"""
>>> sum_two_num_global_local_1()
12
>>> sum_two_num_global_local_2()
102

- The function will first search within the local scope for the variable. If it finds the variable within the local scope, it will use it. 
If it cannot find the variable within the local scope, it will then look for it in the global scope.
For `sum_two_num_global_local_1`, since the variable `num_x` is already found within the local scope (10), thus it did not use the `num_x` define in the global scope (100), thus the total will be equal to 12 (10 + 2)
For `sum_two_num_global_local_2`, since it cannot find the variable `num_y` locally, it looked for it in the global scope, thus total will be equal to 102 (100 + 2)
"""

# References:
# No resources are consulted to solve the given problems