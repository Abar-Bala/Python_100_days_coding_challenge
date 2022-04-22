# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

input_number = 8
input_list = [x for x in range(1,input_number+1)]
result_dict ={}

for index, number in enumerate(input_list,1):
  result_dict[index] = number * number
print(result_dict)