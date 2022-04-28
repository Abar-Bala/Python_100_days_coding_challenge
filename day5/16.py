# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

#i/p:1,2,3,4,5,6,7,8,9
#o/p:1,9,25,49,81

raw_ip=input("enter the list of numbers ")
processed_ip = [int(x) for x in raw_ip.split(",") ]
output_list =[x*x for x in processed_ip if x%2 !=0 ]
print(output_list)