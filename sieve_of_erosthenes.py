import math 
def sieve(n):
	if n <= 2:
		return []
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	
	for i in range(2,math.ceil((math.sqrt(n)))):
		if is_prime:
			for x in range(i*i,n,i):
				is_prime[x] = False
				
	return [i for i in range(n) if is_prime[i]]


print(sieve(50)) #printing prime numbers less than n
print(len(sieve(10050)))



