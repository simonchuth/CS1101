"""
1) There is something wrong with the arguments the function is getting; a precondition is violated (Downey, 2015).

When the function is designed, the author is assuming that the arguments (variables passed into the function) to meet a particular condition/specification.
For the example below, the function is expecting 2 integers as the argument, and it is finding out the value of the product between both number.
If the argument passed into the function violate the expected condition/specification, when the variable is being used to perform a certain operation, it might raise an error.
For the example below, if the 2 string variables were passed into the function,  it will raise an error as the `*` operation is invalid between 2 string variable.
Hence, in this case, the condition/specification before the function execute (pre-condiction) is not being met (violated)

To prevent this from happening, the author could implement some sanity check on the arguments that were passed in, before using them to run the function. 
For the example below, the author could check that the arguments are not string (less stringent), or check that the arguments passed in are either integer or float (more stringent).

References:
Downey, A. (2015). Think Python: How to Think Like a Computer Scientist. Green Tea Press
"""

def calculate_product(a, b):
    return a * b

print(f'When the 2 argument met the condition of the function, both are integers: function returns {calculate_product(2, 5)} \n')

print(f'When the 2 argument violated the condition of the function, both are string: function encounters an error {calculate_product("a", "b")}')

"""
Output of the above script

When the 2 argument met the condition of the function, both are integers: function returns 10 

Traceback (most recent call last):
  File "xxxxxxxxxxxxxxxxxx/discussion_example1.py", line 17, in <module>
    print(f'When the 2 argument violated the condition of the function, both are string: function encounters an error {calculate_product("a", "b")}')
  File "xxxxxxxxxxxxxxxxxx/discussion_example1.py", line 13, in calculate_product
    return a * b
TypeError: can't multiply sequence by non-int of type 'str'
"""