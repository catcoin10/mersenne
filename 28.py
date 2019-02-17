import sys # arguments
#global n, i # allow n and i to be used globally
n = 28 # double Mersenne number
for i in range(2): # do NOT change the number in range(); you could cause memory overflow (this is technically tetration)
	n = (2 ** n) - 1 # we are iterating exponential function twice
i = 2 # number we test
def factor(n, i): # get the factor
	while (n % i) != 0: # do the work in the while statement
		i += 1 # add 1 to the number
#		print(i)
	return i # send the data back
while True: # keep going, there is no need to check (n > i) because doing so takes a significant amount of time
	i = factor(n, i) # run the program
	print(str(i) + " is a factor.") # print string
	i += 1 # keep it going; we don't want it to freeze
