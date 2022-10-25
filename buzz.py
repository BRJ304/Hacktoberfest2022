# Python program to check whether the
# given number is Buzz Number or not.

# function to check BUzz number.
def isBuzz(num) :
	
	# checking if the number
	# ends with 7 and is divisible by 7
	return (num % 10 == 7 or num % 7 == 0)

# Driver method
i = 67
j = 19
if (isBuzz(i)) :
	print ("Buzz Number")
else :
	print ("Not a Buzz Number")
if (isBuzz(j)) :
	print ("Buzz Number")
else :
	print ("Not a Buzz Number")
