"""
Permits exploration of EXPRESSIONS, e.g. 3 + (5 * 2) and "hello" + "goodbye",
and NAMES and ASSIGNMENT, e.g.    n = n + 1

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
"""

import random
import math

###############################################################################
# Done 1: Smile
###############################################################################

###############################################################################
# done 2:18 gal
#   Write a statement that prints your name
print("Belinda")
###############################################################################


###############################################################################
# Part 1: Numbers, Arithmetic, and Precedence.
###############################################################################

###############################################################################
# done: 3.
#   Uncomment the following and then run the program, paying close attention
#   to what gets printed.
#  _
#   Then type an example of your own for each of:
#        -- subtraction
#        -- division
#   and run the program, checking that what gets printed is what you expect.
###############################################################################

print()
print("_done"
      " 3:")
print("4 + 8 evaluates to:   ", 4 + 8)
print("7 * 10 evaluates to:  ", 7 * 10)
print("1.53 + 8 evaluates to:", 1.53 + 8)
print(5 - 2)
print(55 / 11)

###############################################################################
# done
# : 4.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
###############################################################################

print()
print("_done"
      " 4:")
print("(4 + 2) * 3 evaluates to:", (4 + 2) * 3)
print("4 + (2 * 3) evaluates to:", 4 + (2 * 3))
print("4 + 2 * 3   evaluates to:", 4 + 2 * 3)
print("(4 - 2) + 3 evaluates to:", (4 - 2) + 3)
print("4 - (2 + 3) evaluates to:", 4 - (2 + 3))
print("4 - 2 + 3   evaluates to:", 4 - 2 + 3)

###############################################################################
# done
# : 5.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
###############################################################################

# print()
# print("_done
# 5:")
# print("2 ** 10  evaluates to:", 2 ** 10)
# print("10 ** 2  evaluates to:", 10 ** 2)
# print("2 ** 0.5  evaluates to:", 2 ** 0.5)
# print("10 ** -2  evaluates to:", 10 ** -2)
# print("10 ** -0.5  evaluates to:", 10 ** -0.5, "(do you see why?")

###############################################################################
# done: 6.
#   Type some expressions of your own choosing that use combinations of:
#     -- addition, subtraction
#     -- multiplication, division
#     -- exponentiation
#   using parentheses to make clear the order of operations.
#   Then run the program, checking that what gets printed is what you expect.
#  _
###############################################################################

print()
print("_done"
      " 6:")
print(3 + 4 * (9 - 2))
print((3 * 2) / 2)
print(33 ** 2)
###############################################################################
# Part 2: Exceptions: Syntax and Run-Time Errors.
###############################################################################

###############################################################################
# done
# : 7.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the syntax error.
#  _
#   Now type some other statement that causes a syntax error,
#   for example a statement that is missing a required parenthesis.
#   Run again to see the error-message from your syntax error,
#   and finally comment-out your statement to continue to the next _done
#   .
###############################################################################

# print()
# print("_done
# 7:")
# This is crazy!  Python will make no sense of it!

###############################################################################
# done: 8.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed, especially the last red line.
#   Note that the error-output (in red) may (or may not) appear BEFORE the
#   ordinary output from previously executed PRINT statements.
#  _
#   Then comment-out the line that causes the run-time error.
###############################################################################

# print()
# print("_done
# 8:")
# print("3 + 2 evaluates to:", 3 + 2)
# print("3 / 0 evaluates to:", 3 / 0)

###############################################################################
# done
# : 9.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed, especially the last red line.
#   Again note that the error-output (in red) may PRECEDE ordinary output.
#  _
#   Then comment-out the first line that causes the run-time error
#   and run the program again to see the result of running the line below it.
###############################################################################

# print()
# print("_done
# 9:")
# print("3 / 'hello' evaluates to:", 3 / 'hello')

###############################################################################
# done
# : 10.
#   Type some expressions of your own choosing that cause error messages.
#   Then run the program, paying close attention to the last line
#   of each error message (in red).
#  _
###############################################################################

# print()
# print("_done
# 10:")

###############################################################################
# Part 3: Objects, Types, and Values.
###############################################################################

###############################################################################
# done
# : 11.
#   READ the following statements and PREDICT what they will produce as output.
#   Then, uncomment them and run the program, checking your predictions
#   and learning from any predictions that you got wrong
###############################################################################

# print()
# print("_done
# 11:")
#
# print("The type of   482      is:", type(482))
# print("The type of   48.203   is:", type(48.203))
# print('The type of   "blah blah blah"      is:', type("blah blah blah"))
# print("The type of   'blah blah blah'      is:", type('blah blah blah'))
# print("The type of   [4, 2, 9]      is:", type([4, 2, 9]))
# print("The type of   (4, 2, 9)      is:", type((4, 2, 9)))
# print("The type of   min     is:", type(min))
# print("The type of   'min'   is:", type('min'))
# print("The type of   min(4, 6, 2, 12, 10)    is:", type(min(4, 6, 2, 12, 10)))
# print("The type of   min(4, 6, 2.0, 12, 10)  is:", type(min(4, 6, 2.0, 12, 10)))


###############################################################################
# done
# : 12.
#   Type an expression that involves addition, subtraction and multiplication
#   (but NOT division, yet), using whole numbers (which are of type int).
#   Then run the program, checking that what gets printed is what you expect.
#  _
#   Next, repeat the above, but making just a single one of the numbers in
#   your expression a float, by appending a decimal point to it, like this:
#       instead of 2 (which is an int), write 2.0 (which is a float).
#  _
#  Finally, try division by uncommenting the following and then run the program,
#  paying close attention to what gets printed.  What do you notice about the
#  type that results from division, even if both arguments are  int  objects?
###############################################################################

# print()
# print("_done
# 12:")
# print("4.2 / 2.0 evaluates to:", 4.2 / 2.0)
# print("4.2 / 2   evaluates to:", 4.2 / 2)
# print("4 / 2     evaluates to:", 4 / 2)
# print("3 / 2     evaluates to:", 3 / 2)

###############################################################################
# done
# : 13.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#  Then try more expressions involving the   //   and   %   operators
#  until you understand what those operators do.
###############################################################################

# print()
# print("_done
# 13:")
# print("17 // 5   evaluates to:", 17 // 5)
# print("17 % 5    evaluates to:", 17 % 5)

###############################################################################
# done
# : 14.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#  Then try more expressions involving string arithmetic as needed, until you
#  understand what the  +   and   *   operators do when applied to strings.
###############################################################################

# print()
# print("_done
# 14:")
#
# print("hello" + "goodbye girl")
# print("big" * 20)
# print(("hello " + "goodbye ") * 4)

###############################################################################
# done
# : 15.
#   Type a statement that prints:
#     I'm not a bug, that's right!
#   and then run the program, checking that it printed the above sentence
#   (including the punctuation exactly as written above).
#  _
#   Then repeat the above for the sentence:
#     What does "yarborough" mean?
#  _
#   Then repeat the above for the sentence:
#     I'm on "pins and needles" about '"'".
#   Hint: consider using the   +   operator as part of your solution.
#  _
###############################################################################

# print()
# print("_done
# 15:")

###############################################################################
# Part 4: Names, Variables, and Assignment.
###############################################################################

###############################################################################
# done
# : 16.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the run-time error,
#   PREDICT what the subsequent lines will print,
#   and run again to check your predictions.
#  _
#   Finally, practice assignment as suggested by the examples below, that is:
#   choose your own names, given them values by using the assignment (=)
#   operator, and define new names by using expressions that include names
#   that you defined previously.
###############################################################################

# print()
# print("_done
# 16:")
# first_program = "Hello, world!"
# print(first_program)
# print(greeting)
#
# greeting = "Hello, earthlings"
# print(greeting)
# print(first_program + (greeting * 2))
#
# n = 3
# print(first_program * n)
# n = 2 * first_program
# print(n + greeting)

###############################################################################
# done
# : 17.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Throughout this program, remember that error-output may (or may not)
#   PRECEDE ordinary output from previous PRINT statements.  Be sure to scroll
#   up to see if any error message (in red) appears higher up in the Console.
#  _
#   Then repeatedly:
#     -- comment-out the line that causes a run-time error
#     -- run again to see the output from the statements that follow it.
#   until you see the output from the last statement below,
#   noting its perhaps-surprising output.
#  _
#   Finally, try out your own assignment statements that yield run-time errors.
###############################################################################

print()
print("_done"
      " 17:")
r = 2
s = -9
t = s / r
y = 2 + s
u = math.sqrt(2)
v = (2) ** 0.5
print(v)

###############################################################################
# done
# : 18.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the run-time error,
#   PREDICT what the subsequent lines will print,
#   and run again to check your predictions.
###############################################################################

# print()
# print("_done
# 18:")
# a = 45
# 45 = a
# b = 10
# c = b + 20
# b = c
# print(a, b, c)

###############################################################################
# done
# : 19.
#   Uncomment the following and PREDICT what will get printed.
#   Then run the program, checking to see whether your prediction is correct.
###############################################################################

# print()
# print("_done
# 19:")
# x = 5
# x = x + 1
# print(x)
#
# x = x + 1
# print(x)
#
# x = x + 1
# print(x)

###############################################################################
# done
# : 20.
#   Uncomment the following and PREDICT what will get printed.
#   (Hint: what gets printed is  NOT  75 10.)
#   Then run the program, checking to see whether your prediction is correct.

###############################################################################
# done
# : 21.
#  The statements below make x and y refer to random integers between 1 and 99,
#  then prints the values of x and y.
#  _
#  Challenge: can you write statements below the following that causes the
#    values of x and y to SWAP?  For example, if the values of x and y are set
#    randomly to 40 and 33, so that the given print statement prints:  40 33
#    then your code should print:  33 40
#  _
#  Spend up to 1 minute on this challenge, typing your code and running the
#  program to try out your solution.
#  _
###############################################################################

print()
print("_done"
      " 22:")
x = random.randint(1, 99)
y = random.randint(1, 99)
print(y, x)
print(x, y)
