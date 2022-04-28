# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# i/p: 
# D 300
# D 300
# W 200
# D 100

# o/p:
# 500

A = 0
ip_list =[]

while True:
  ip = input()
  if ip:
    ip_list.append(ip.split(" "))
  else:
      break
for entry in ip_list:
  if entry[0] == "D":
    A += int(entry[1])
  elif entry[0] == "W":
    A -= int(entry[1])

print(f"your account balance {A}")