def repeat_myself(n):
    print('Current recurssion depth: {}'.format(n))
    repeat_myself(n + 1)

repeat_myself(1)