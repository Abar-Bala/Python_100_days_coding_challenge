# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

#i/p: Hello world!
# UPPER CASE 1
# LOWER CASE 9

from collections import Counter

UPPER_CASE = LOWER_CASE = 0
raw_input = input("enter the sentence ")
input_dict = Counter(raw_input)
for k,v in input_dict.items():
  if k.islower():
    LOWER_CASE += v
  elif k.isupper():
    UPPER_CASE += v

print(f"UPPER CASE {UPPER_CASE} \n LOWER CASE {LOWER_CASE}")
  
  