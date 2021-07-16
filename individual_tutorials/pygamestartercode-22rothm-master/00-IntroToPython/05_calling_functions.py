"""
Permits exploration of CALLING FUNCTIONS and CALLING METHODS.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
"""

###############################################################################
# Done 1: Smile
###############################################################################

###############################################################################
# Done 2:
#   Write a statement that prints your name twice
#     Can you do this in a single statement? Ask your instructor for tips.
###############################################################################
import random

print("Task 2")
print("Marisa Roth " *2)
###############################################################################
# Part 1: Calling FUNCTIONS.
###############################################################################

###############################################################################
# Done: 3.
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
print("Task 3")
import math
def main():
    cosine(math.cos(2.5))
    degree(math.radians(-0.5))
    log(math.log(e, -2))
    factorial(math.factgorial(100))
    lgamma(math.lgamma(3.1))

###############################################################################
# Done: 4.
#   Type the statements needed to print a random integer between 100 and 1000,
#   using the   random.randint   function to do so.
#   Run the program to test your statements.
#  _
#   After doing so, bring up the Quick Documentation for random.randint.
###############################################################################
print("Task 4")
print(random.randint(100, 1000))
###############################################################################
# Done: 5.
#   Below this _TODO, put statements that call functions defined
#   in the   builtins   module to do each of the following,
#   running the program after typing each, to test your statements one by one:
#     -- the absolute value of a random integer between -100 and 100
#     -- the smallest of 4 randomly-chosen integers between 1 and 20
#   The result will be different each time you run the program,
#   because of the randomness.
###############################################################################
print("Task 5")
x= random.randint(-100, 100)
print(math.fabs(x))
###############################################################################
# Done: 6.
#   The code below defines a function that returns the temperature
#   in Celsius of a given temperature in Fahrenheit.
#   BELOW that function definition, write code that prints:
#     -- the temperature in Celsius of 1000 degrees Fahrenheit
#     -- the temperature in Celsius of -80 degrees Fahrenheit
###############################################################################
print("task 6")

def get_celsius(temperature_in_fahrenheit):
    return (temperature_in_fahrenheit - 32) * (5 / 9)

x = get_celsius(100)
print(x)

y = get_celsius(-80)
print(y)




