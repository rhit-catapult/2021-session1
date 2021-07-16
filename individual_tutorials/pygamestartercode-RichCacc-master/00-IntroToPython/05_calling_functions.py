import math
import random

"""
Permits exploration of CALLING FUNCTIONS and CALLING METHODS.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
"""

###############################################################################
# DONE 1: Smile
###############################################################################

###############################################################################
# Done 2:
#   Write a statement that prints your name twice
#     Can you do this in a single statement? Ask your instructor for tips.
###############################################################################
print(2 * "Richard ")
###############################################################################
# Part 1: Calling FUNCTIONS.
###############################################################################

###############################################################################
# DONE: 3.
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
print()
print("Done 3")
funky1 = math.cos(2.5)
funky2 = math.degrees(-0.5)
funky3 = math.log(math.e, 2)
funky4 = math.factorial(100)
funky5 = math.lgamma(3.1)
print(funky1)
print(funky2)
print(funky3)
print(funky4)
print(funky5)
###############################################################################
# DONE: 4.
#   Type the statements needed to print a random integer between 100 and 1000,
#   using the   random.randint   function to do so.
#   Run the program to test your statements.
#  _
#   After doing so, bring up the Quick Documentation for random.randint.
###############################################################################
print()
print("DONE 4")
print(random.randint(100, 1000))
###############################################################################
# DONE: 5.
#   Below this _TODO, put statements that call functions defined
#   in the   builtins   module to do each of the following,
#   running the program after typing each, to test your statements one by one:
#     -- the absolute value of a random integer between -100 and 100
#     -- the smallest of 4 randomly-chosen integers between 1 and 20
#   The result will be different each time you run the program,
#   because of the randomness.
###############################################################################
print()
print("DONE 5")
abs1 = abs(random.randint(-100, 100))

small = random.randint(1, 20)
last = small
print(small)
stop4 = 1
while stop4 <= 3:
    small = random.randint(1, 20)
    print(small)
    if small < last:
        last = small
    stop4 = stop4 + 1
print(last)
###############################################################################
# TODO: 6.
#   The code below defines a function that returns the temperature
#   in Celsius of a given temperature in Fahrenheit.
#   BELOW that function definition, write code that prints:
#     -- the temperature in Celsius of 1000 degrees Fahrenheit
#     -- the temperature in Celsius of -80 degrees Fahrenheit
###############################################################################
print()
print("DONE 6")

def main():
    get_celsius(1000)
    get_celsius(-80)

def get_celsius(temperature_in_fahrenheit):
    """
    Returns the temperature in Celsius of the given Fahrenheit temperature.
    For example, this function returns   XXX   when given   YYY.

    Type hints:
      :type temperature_in_fahrenheit: float
    """
    print((temperature_in_fahrenheit - 32) * (5 / 9))

main()

