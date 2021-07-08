# Python3 implementation of the
# above approach

# Function to generate random numbers
def multiplicativeCongruentialMethod(Xo, m, a,
									randomNums,
									noOfRandomNums):

	# Initialize the seed state
	randomNums[0] = Xo

	# Traverse to generate required
	# numbers of random numbers
	for i in range(1, noOfRandomNums):

		# Follow the linear congruential method
		randomNums[i] = (randomNums[i - 1] * a) % m

# Driver Code
if __name__ == '__main__':

	# Seed value
    Xo = int(input("Enter Xo: "))

	# Modulus parameter
    m = int(input("Enter m: "))
	# Multiplier term
    a = int(input("Enter a: "))

	# Number of Random numbers
	# to be generated
    noOfRandomNums = int(input("Enter Number of Random Numbers: "))

	# To store random numbers
    randomNums = [0] * (noOfRandomNums)

	# Function Call
    multiplicativeCongruentialMethod(Xo, m, a,
									randomNums,
									noOfRandomNums)

	# Print the generated random numbers
    for i in randomNums:
	    print(i)
