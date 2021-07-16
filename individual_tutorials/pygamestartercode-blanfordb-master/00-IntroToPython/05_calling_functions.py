"""
Permits exploration of CALLING FUNCTIONS and CALLING METHODS.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
"""
import math
import random
###############################################################################
# TODOne 1: Smile
###############################################################################

###############################################################################
# TODOne 2:
#   Write a statement that prints your name twice
#     Can you do this in a single statement? Ask your instructor for tips.
###############################################################################
print("braden blanford " * 2)
###############################################################################
# Part 1: Calling FUNCTIONS.
###############################################################################

###############################################################################
# TODOne: 3.
#   Recall that a FUNCTION gives a NAME to a block of code,
#   and can have (and usually does have) PARAMETERS that receive values
#   from actual ARGUMENTS when the method/function is CALLED.
#  _
#   Put a statement at the beginning of this module (near line 9)
#   that imports the   math   module.
#  _
#   Then, below this _TODO, put statements that call functions defined
#   in the math module to do each of the following, running the program
#   after typing each, to test your statements one by one:
#     -- the cosine of 2.5
#     -- the degrees that is the equivalent of -0.5 radians
#     -- The base-2 logarithm of the constant   e   where you use the math
#          module to access the value of the constant   e.
#     -- The result of applying the   factorial   function to the argument 100,
#          that is,   100!
#     -- The result of applying the   lgamma     function to the argument 3.1.
#   After you do the last of the above, hover over the function name  lgamma
#   to see its Quick Documentation.
###############################################################################
print(math.cos(2.5))
print(math.degrees(-0.5))
print(math.log(math.e, 2))
print(math.factorial(100))
print(math.lgamma(3.1))
###############################################################################
# TODOne: 4.
#   Type the statements needed to print a random integer between 100 and 1000,
#   using the   random.randint   function to do so.
#   Run the program to test your statements.
#  _
#   After doing so, bring up the Quick Documentation for random.randint.
###############################################################################
print(random.randint(4, 10))
###############################################################################
# TODOne: 5.
#   Below this _TODO, put statements that call functions defined
#   in the   builtins   module to do each of the following,
#   running the program after typing each, to test your statements one by one:
#     -- the absolute value of a random integer between -100 and 100
#     -- the smallest of 4 randomly-chosen integers between 1 and 20
#   The result will be different each time you run the program,
#   because of the randomness.
###############################################################################
print(math.fabs(random.randint(-100, 100)))
print(min(random.randint(1, 20), (random.randint(1, 20)), (random.randint(1, 20)), (random.randint(1, 20))))
###############################################################################
# TODOne: 6.
#   The code below defines a function that returns the temperature
#   in Celsius of a given temperature in Fahrenheit.
#   BELOW that function definition, write code that prints:
#     -- the temperature in Celsius of 1000 degrees Fahrenheit
#     -- the temperature in Celsius of -80 degrees Fahrenheit
###############################################################################
def get_celsius(temperature_in_fahrenheit):
    """
    Returns the temperature in Celsius of the given Fahrenheit temperature.
    For example, this function returns   XXX   when given   YYY.

    Type hints:
      :type temperature_in_fahrenheit: float
    """
    return (temperature_in_fahrenheit - 32) * (5 / 9)
print(get_celsius(1000))
print(get_celsius(-80))
