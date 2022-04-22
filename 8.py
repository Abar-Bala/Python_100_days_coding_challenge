# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program:
#i/p: without,hello,bag,world
#o/p: bag,hello,without,world

raw_input = input("enter the word list ")
processed_input = [x for x in raw_input.split(",")]
processed_input.sort()
print(",".join(processed_input))
