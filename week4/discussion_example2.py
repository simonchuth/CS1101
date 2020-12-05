"""
2) There is something wrong with the function; a postcondition is violated (Downey, 2015).

This means that the author have made an error in the code of the function. Hence, when the code executes, it will raise an error.
In the example below, there is a syntax error (the variable answer should be on the left side of the assign statement), thus when the function is being called, it will raise a syntax error, due to a mistake made in the code.
Hence in this case, the error (violation) is due to an issue after (post) the condition have been met, thus the postcondition is violated.

References:
Downey, A. (2015). Think Python: How to Think Like a Computer Scientist. Green Tea Press
"""

def calculate_product(a, b):
    a * b = answer
    return answer

print(f'Although both variable are integers (met the condition), it will still raise an error, due to the syntax error in the function {calculate_product(2, 5)} \n')

"""
Output of the above script

When the 2 argument met the condition of the function, both are integers: function returns 10 

Traceback (most recent call last):
  File "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/discussion_example1.py", line 17, in <module>
    print(f'When the 2 argument violated the condition of the function, both are string: function encounters an error {calculate_product("a", "b")}')
  File "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/discussion_example1.py", line 13, in calculate_product
    return a * b
TypeError: can't multiply sequence by non-int of type 'str'
"""