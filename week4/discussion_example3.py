"""
3) There is something wrong with the return value or the way it is being used (Downey, 2015).

This means that there are nothing logically wrong with the arguments, and the function executed without raising any error.
However, the arguments passed in the function might be of the wrong type, but it is still logically correct in the function, thus the returned variable will be of the wrong type. 
Hence, when the variable is being used, it might result in an error.
In addition, the arguments and function might have executed as expected, but the downstream function might have used the returned value wrongly, thus raising an error.

References:
Downey, A. (2015). Think Python: How to Think Like a Computer Scientist. Green Tea Press
"""

def calculate_product(a, b):
    return a * b

# Correct arguments, functions returned correct value. However, the return value was being used wrongly
context = 'This is a string'
concat_str = context + calculate_product(1, 4)  # The function returned an int as expected, but you can't concatenate a str and int together

"""
Output for this part of the script

Traceback (most recent call last):
  File "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/discussion_example3.py", line 18, in <module>
    concat_str = context + calculate_product(1, 4)
TypeError: can only concatenate str (not "int") to str
"""

# Wrong arguments, functions returned wrong value.
answer = 5 + calculate_product('1', 4)  # The function returned a str, because '1' is a string, when passed into the function, it will return '1111' as a string, which cannot be added (concatenate) to an int

"""
Output for this part of the script

Traceback (most recent call last):
  File "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/discussion_example3.py", line 18, in <module>
    answer = 5 + calculate_product('1', 4)  # The function returned a str, because '1' is a string, when passed into the function, it will return '1111' as a string, which cannot be added (concatenate) to an int     
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
