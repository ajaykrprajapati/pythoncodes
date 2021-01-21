#First Class Function :
# It supports all the operations genrally available to other entitites. These operation enerally include being passed as an argument,returned from a function, and assigned to a var.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1') #constant tag assinged for other to follow, return dynamic method to print msg
print_h1('Test Headline!')  # pass msg to print in defined manner
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')

# Closures
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)


# Decorators
'''In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
Functions can be defined inside another function and can also be passed as argument to another function.

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.'''

@gfg_decorator
def hello_decorator():
    print("Gfg")


'''Above code is equivalent to - 

hello_decorator = gfg_decorator(hello_decorator)'''


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)


# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time














##Coding guidlines:
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Use range function to loop over a series of numbers
#=====================================================
# Non Pythonic
for i in [0, 1, 2, 3, 4, 5]:
    print(i * i)

# Pythonic

for i in range(0, 6):  # python 3
    print(i * i)


#Looping over a collection
#============================

# Non Pythonic
names = ['james', 'jack', 'alex', 'martin']
# Forward looping
for i in range(len(names)):
    print(names[i])
# Reverse looping
for i in range(len(names)-1, -1, -1):
    print(names[i])
# Print indices with names
for i in range(len(names)):
    print(i, '--->', names[i])

# Pythonic
names = ['james', 'jack', 'alex', 'martin']
# Forward looping
for name in names:
    print(name)
# Reverse looping of names
for name in reversed(names):
    print(name)
# Print indices with names
for i, name in enumerate(names):
    print(i, '---->', name)

# looping over two collections together
names = ['james', 'jack', 'alex', 'martin']
ages = [23, 34, 54]
# Non pythonic
n = min(len(names), len(ages))
for i in range(n):
    print(names[i], '--->', ages[i])
# Pythonic
for name, age in zip(names, ages):
    print(name, '---->', age)

