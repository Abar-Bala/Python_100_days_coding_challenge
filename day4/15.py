# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#i/p: 9
#o/p: 11106

raw_ip = input("enter the number ")
int_ip = int(raw_ip)
print(int_ip)

output = int_ip + 2*int_ip + 3*int_ip + 4*int_ip

print(output)

# a = input()
# total = int(a) + int(2*a) + int(3*a) + int(4*a)  
# N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
# print(total)

