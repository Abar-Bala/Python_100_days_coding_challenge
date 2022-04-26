# Write a program that accepts a sentence and calculate the number of letters and digits.

# i/p:hello world! 123
# o/p:LETTERS 10
#     DIGITS 3
from collections import Counter 
LETTERS=DIGITS = 0


raw_input = input("enter a sentence ")
input_dict=Counter(raw_input)
for k,v in input_dict.items():
  if k.isdigit():
    DIGITS += v 
  elif k.isalpha():
    LETTERS += v

print(f"LETTERS {LETTERS} \n DIGITS {DIGITS}")