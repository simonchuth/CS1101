"""
In chained conditional, the condition for each if (and elif) statements were checked in order. 
When one of the condition have been met, it will not proceed with the subsequent conditions (Downey, 2015).
For nested conditional, not all the conditions will be assess in order. Hence, nested conditional will be more efficient.

References:
Downey, A. (2015). Think Python: How to Think Like a Computer Scientist. Green Tea Press
"""

import time

# Chained conditional
def test_chained(x):
    start_time = time.time()
    if x < 100:
        return (time.time() - start_time)
    elif x < 200:
        return (time.time() - start_time)
    elif x < 300:
        return (time.time() - start_time)
    elif x < 400:
        return (time.time() - start_time)
    elif x < 500:
        return (time.time() - start_time)
    elif x < 600:
        return (time.time() - start_time)
    elif x < 700:
        return (time.time() - start_time)
    elif x < 800:
        return (time.time() - start_time)
    elif x < 900:
        return (time.time() - start_time)
    elif x < 1000:
        return (time.time() - start_time)
    elif x < 1100:
        return (time.time() - start_time)
    else:
        return (time.time() - start_time)

# Nested conditional
def test_nested(x):
    start_time = time.time()
    if x < 500:
        if x < 250:
            if x < 100:
                return (time.time() - start_time)
            else:
                if x < 200:
                    return (time.time() - start_time)
                else:
                    return (time.time() - start_time)
        else:
            if x < 300:
                return (time.time() - start_time)
            else:
                if x < 400:
                    return (time.time() - start_time)
                else:
                    return (time.time() - start_time)
    else:
        if x < 1000:
            if x < 750:
                if x < 600:
                    return (time.time() - start_time)
                else:
                    if x < 700:
                        return (time.time() - start_time)
                    else:
                        return (time.time() - start_time)
            else:
                if x < 800:
                    return (time.time() - start_time)
                else:
                    if x < 900:
                        return (time.time() - start_time)
                    else:
                        return (time.time() - start_time)
        else:
            return (time.time() - start_time)

loop_size = 1000000

x = 1100
print(f'\nTarget variable = {x}')
chained_time_list = [test_chained(x) for i in range(loop_size)]
total_chained_time = sum(chained_time_list)
print(f'Time taken for chained conditional: {total_chained_time} seconds for {loop_size} loops')
nested_time_list = [test_nested(x) for i in range(loop_size)]
total_nested_time = sum(nested_time_list)
print(f'Time taken for nested conditional: {total_nested_time} seconds for {loop_size} loops')

x = 910
print(f'\nTarget variable = {x}')
chained_time_list = [test_chained(x) for i in range(loop_size)]
total_chained_time = sum(chained_time_list)
print(f'Time taken for chained conditional: {total_chained_time} seconds for {loop_size} loops')
nested_time_list = [test_nested(x) for i in range(loop_size)]
total_nested_time = sum(nested_time_list)
print(f'Time taken for nested conditional: {total_nested_time} seconds for {loop_size} loops')
