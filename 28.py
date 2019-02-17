# get the numbers for 28th Mersenne prime
import sys # arguments
n = 28 # double Mersenne number
for i in range(2): # do NOT change the number in range(); you could cause memory overflow (this is technically tetration)
	n = (2 ** n) - 1 # we are iterating exponential function twice
i = int(sys.argv[1]) # number we test
while (n % i) != 0: # do the work in the while statement
	i += 1 # add 1 to the number
	print(i)
print(str(i) + " is a factor")
