# Decorators

""" Example 1 of a closure
def outer_function():
  message = 'Hi'
  # inner funcion within outer function:
  def inner_function():
    print(message)
  # returns 'Hi' as function is executed
  return inner_function()

outer_function() """

""" Example 2 of a closure: same example as 1 but now returning inner_function without executing it:

def outer_function():
  message = 'Hi'
  # inner funcion within outer function:
  def inner_function():
    print(message)
  # returns 'Hi' as function is executed
  return inner_function

# The message variable is accessed by inner_function()
# and returned by outer_function through inner_function
my_func = outer_function()
my_func() # prints "Hi"
my_func()
my_func() """

""" Example 3 of a closure
now outer_function() has a param
def outer_function(msg):
  def inner_function():
    print(msg)
  return inner_function()

hi_func = outer_function('Hi') # prints 'Hi
bye_func = outer_function('Bye') # prints "Bye" """

"""
What is a decorator?  A decorator is a function that takes another function as a argument, adds some kind of functionality, and then returns another function, all of this without altering the source code of the original function that you passed in.
"""

# Example 1 of decorator function

""" def decorator_function(original_function):
  def wrapper_function():
    return original_function()
  return wrapper_function

def display():
  print('display function ran')
  
decorated_display = decorator_function(display)
decorated_display() """ # prints "display function ran"

"""
Why use a decorator? They allow to easily add functionality to existing functions by adding that functionality inside a wrapper. 
"""

""" Example 1:
def decorator_function(original_function):
  def wrapper_function():
    print(f'wrapper executed this before {original_function.__name__} ')
    return original_function()
  return wrapper_function

# @decorator_function == decorator_function(display)
def display():
  print('display function ran')
  
decorated_display = decorator_function(display)
decorated_display()

prints "wrapper executed this before display"
prints "display function ran" 
"""

# Example 1, now with @:
""" def decorator_function(original_function):
  def wrapper_function():
    print(f'wrapper executed this before {original_function.__name__} ')
    return original_function()
  return wrapper_function

@decorator_function
def display():
  print('display function ran')

display() """

"""
Example 2 with *args and **kwargs

def decorator_function(original_function):
  # args and kwargs required inside wrapper function definition if the original function is called with any args and kwargs:
  def wrapper_function(*args, **kwargs):
    print(f'wrapper executed this before {original_function.__name__} ')
    # args and kwargs required here too:
    return original_function(*args, **kwargs)
  return wrapper_function

@decorator_function
def display():
  print('display function ran') 
  
@decorator_function
def display_info(name, age):
  print(f'display_info ran with arguments {name}, {age}')


#info printed in console: 
#wrapper executed this before display_info 
#display_info ran with arguments John, 25
#wrapper executed this before display
#display function ran

  
display_info('John', 25)
display()
"""

# Example 3: using classes as decorators

class decorator_class(object):
  
  def __init__(self, original_function):
    self.original_function = original_function
    
  def __call__(self, *args, **kwds):
    print(f'call method executed this before {self.original_function.__name__}')
    return self.original_function(*args, **kwds)

@decorator_class
def display():
  print('display function ran')
  
@decorator_class
def display_info(name, age):
  print(f'display_info ran with arguments {name}, {age}')
  
display_info('John', 25)
display()