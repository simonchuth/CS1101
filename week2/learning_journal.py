# Part 1
def print_volume(radius):
    """ GIven radius of sphere, calculate and print volume of sphere

    :param radius: Radius of sphere
    :type radius: float or int
    """
    pi = 3.141592653589793
    volume = (4/3)*pi*radius**3
    print(volume)

print('Radius of 2')
print_volume(2)
print('Radius of 5')
print_volume(5)
print('Radius of 10')
print_volume(10)

# Part 2
def greet(your_name, greetings, echo=1):
    """ Print out greetings to a person, and echo the greetings

    :param your_name: Name of person
    :type your_name: str
    :param greetings: Words to greet the person with
    :type greetings: str
    :param echo: Number of times to repeat the greetings, defaults to 1
    :type echo: int, optional
    """
    output = greetings + ' ' + your_name + '!\n'  # `+` concatenate string together, and `\n` in string means next line
    output = output * echo  # `*` when used in string, will repeat the string
    print(output)

greet('Tom', 'Hello', echo=3)
greet('Mary', 'Goodbye', echo=5)
greet('Tim', 'Hey', echo=3)


