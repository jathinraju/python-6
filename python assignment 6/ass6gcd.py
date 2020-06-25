#prgm on gcd
n1 = int(input("enter a n1 number :"))
n2 = int(input("enter a n2 number :"))
while n1 is not n2 :
	if n1>n2 :
		n1 = n1-n2
	else :
		n2 = n2-n1
else :
		print("the gcd of n1 and n2 is : ",n1)
		