def isPrime(n):
	for i in range(2,n):
		if n % i == 0:
			return n

result = filter(isPrime,range(1,100))
print result