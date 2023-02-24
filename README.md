# Recursive-Counting-Functions
A collection of recursive functions to count up or down from a given starting value to an end value with or without a specified increment, including options for exclusive or inclusive ending values.

## This repository contains four recursive counting functions implemented in Python.
#### ‣ count_up(start, end): This function takes two arguments, start and end, and outputs a count starting from start until end (excluding end). It does not include an increment value and assumes a step size of 1.

#### ‣ count(start, end): This function takes two arguments, start and end, and outputs a count starting from start and continuing either upward or downward until it reaches end (excluding end). The direction is determined by whether start is greater than or less than end. It assumes a step size of 1.

#### ‣ count_inc(start, end, inc): This function takes three arguments, start, end, and inc, and outputs a count starting from start and continuing either upward or downward until it reaches or exceeds end. The direction is determined by whether start is greater than or less than end. It includes an increment value inc that determines the step size.

#### ‣ count_inc_end(start, end, inc, is_exclusive): This function behaves exactly like count_inc(), but with one modification: a Boolean value for is_exclusive determines whether the function is exclusive (True) or inclusive (False). If is_exclusive is True, the function will stop when it reaches the value of end without including it in the output. If is_exclusive is False, the function will include end in the output.

## Usage
To use any of these functions, simply call the function with the appropriate arguments. For example:
#### count_up(1, 5)
This will output a count starting from 1 and ending at 4.

## Testing
The repository also includes test cases for each of the four functions. To run the tests, simply run the test.py file:

