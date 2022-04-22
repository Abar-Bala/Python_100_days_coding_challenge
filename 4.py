# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

input_list = input('enter list of numbers')
input_list = input_list.split(',')
result_list=[]

for char in input_list:

  
  number = int(char)
  result_list.append(number)

print(f"result list {result_list}")
print(f"result tuple {tuple(result_list)}")