# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.


# for number in range(1000,3000):
#   return number if number % 2 == 0


output =[str(x) for x in range(1000,3001) if x%2 == 0]
print(",".join(output))