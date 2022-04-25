# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#i/p: 0100,0011,1010,1001
#o/p: 1010

raw_input = input("enter the binary number: ").split(",")


def StrToBin(s1):
  int_num = 0
  exp_count=0
  for index in range(len(s1)-1,-1,-1):
    int_num += int(s1[index])* pow(2,exp_count)
    exp_count += 1
  
  return s1 if not int_num%5 else None

print(list(filter(None,(list(map(StrToBin,raw_input))))))




