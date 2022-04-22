# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

#output:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


raw_input = input("enter two numbers ")
#this is an improvement over manual multistep processing
processed_input = [int(x) for x in raw_input.split(",")]
#this is an improvement in terms of good coding practice
X = processed_input[0]
Y = processed_input[1]
output_matrix =[]

for i in range(X): 
  row=[]
  for j in range(Y):
    cell = i*j
    row.append(cell)
  output_matrix.append(row)

print(output_matrix)