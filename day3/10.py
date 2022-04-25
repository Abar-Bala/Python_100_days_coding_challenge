# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

#i/p: hello world and practice makes perfect and hello world again


#o/p: again and hello makes perfect practice world

raw_input = input("enter the input: ")
#removes duplicates
processed_input = set(raw_input.split(" "))
print(" " .join(sorted(processed_input)))

