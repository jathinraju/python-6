#prgm on first N number of fibonacci integers
n = int(input("enter how many fibonacci numbers you want"))
first = 0
second = 1
i = 3
print(first)
print(second)
while i<=n :
	fibo = first + second
	print(fibo ,)
	first = second
	second = fibo
	i+=1
	
	