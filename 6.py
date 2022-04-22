# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input :100,150,180
#output : 18,22,24
import math

input_list = input("enter the numbers ")
C= 50
H= 30

input_numbers=input_list.split(",")

#Method1 following regular scripting style
for number in input_numbers:
  calculated_value = math.sqrt((2*C*int(number))/H)
  output_list.append(round(calculated_value))

#*****************************************
#Method2 following functional programming
def sqrt_cal(number):
  return round( math.sqrt((2*C*int(number))/H))

answer = list(map(sqrt_cal,input_numbers))
print(answer)
  
  