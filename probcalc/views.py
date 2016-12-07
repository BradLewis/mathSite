from django.shortcuts import render
from decimal import Decimal

def index(request):
	print(getNumber("0.8"))
	prevEntry = ""
	try:
		#Gets the probability from the textbox
		n = request.GET['prob']
	except:
		#If there is no prob entered, then prompt user to enter a number
		probStatement = "Enter a value to see the probability!"
		context = {"probability": probStatement, "currentEntry": prevEntry}
		return render(request, 'probcalc/index.html', context)

	#This is just so the textbox holds the value
	prevEntry = n
	#Calculate the probability based on n
	probStatement = getNumber(n)
	context = {"probability": probStatement, "currentEntry": prevEntry}
	return render(request, 'probcalc/index.html', context)

#This function calculates the probability of the scenario. The probability of the given senario is
#p(n) = n!/n^n, which can be simplifed to
#p(n) = (n-1)!/n^(n-1)
def calcProbability(n, nMax):
	#If n is greater than around 900, the function returns 0 anyways so this saves the program crashing for large numbers and recursion
	#errors (python defaults to 1000 max, which works nicely for this solution)
	if n > 900:
		return 0
	#If n is 1 or 0 then do nothing (that is return 1)
	elif n <= 1:
		return 1
	else:
		#We calculate the probability this way other than the more direct way of just n!/n^n as it allows us
		#to calculate the values for much larger n (though it gets rounded to zero after around n=900)
		return (n-1)/(nMax)*calcProbability(n-1, nMax)

def getNumber(n):
	try:
		n = int(n)
		#Statement does not make sense for numbers less than zero
		if n <= 0:
			probStatement = "You cannot have a {0} sided dice! Please enter a valid number".format(n)
		else:
			probability = calcProbability(n, n)
			#Don't need to format if the number is zero
			if probability != 0:
				if probability < 0.00001:
					#Only shows number to 4 decimal places and in scientific notation
					probability = '%.4E' % Decimal(probability)
				else:
					#Shows only 5 decimal places
					probability = '{0:.5f}'.format(probability)
			else:
				#If it shows as zero then say approxiamtely
				probability = 'approximately 0'
			probStatement = "The probability of rolling a {0} sided dice {0} times and each side comes up only once is {1}".format(n, probability)
	except ValueError:
		probStatement = "Whoops! That is not a valid number, please enter a valid number (remember a dice can only have an integer number of sides)"
	except:
		probStatement = "Whoops! That is not a valid number, please enter a valid number"
	return probStatement
