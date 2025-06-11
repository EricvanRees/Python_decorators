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

def decorator_function(original_function):
  def wrapper_function():
    return original_function()
  return wrapper_function

def display():
  print('display function ran')
  
decorated_display = decorator_function(display)
decorated_display() # prints "display function ran"