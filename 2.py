# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
from functools import reduce
input_number = 5
number_list=[x for x in range(1,input_number+1)]
print(reduce(lambda x, y: x*y, number_list))

