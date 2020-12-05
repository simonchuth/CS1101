def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n - 1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

input_num = int(input('Choose a number: '))
if input_num >= 0:
    countdown(input_num)
else:
    countup(input_num)