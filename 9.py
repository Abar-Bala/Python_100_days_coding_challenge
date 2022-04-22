# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

#i/p: Hello world
#     Practice makes perfect

#o/p: HELLO WORLD
#     PRACTICE MAKES PERFECT
lines =[]
while True:
  raw_sentence = input("enter the sentence ")
  if raw_sentence:
    lines.append(raw_sentence.upper())
  else:
    break

print(",".join(lines))