# WD Python
# Example file to illustrate the use of the PythonExecute function
from math import *

# Returns a string
def HelloWorld():
	return "Hello World!"
	
# Returns a completed string with the string received as parameter
def SayHello(name):
	return "Hello, %s" % name

# Returns an integer representing the addition between the two integers received as parameters
def AddInteger(int1, int2):
    return int1 + int2
		
# Returns a float representing the subtraction between the two floats received as parameters
def SubtractFloat(float1, float2):
    return float1 - float2
	
# Returns an array of prime numbers
def ListPrimes(max):
  tabPrime = list(range(2,max+1))
  k = 2
  nRoot = sqrt(max)
  while k < nRoot:
    tabPrime=[p for p in tabPrime if p <= k or p%k != 0]
    k = tabPrime[tabPrime.index(k) + 1]  # new prime number
  return tabPrime

# Returns a dictionary
def ReadDictionary():
	return { "G. Washington": 1732, "C. de Gaulle": 1890, "Nabuchodonosor II": -642 }
	
# Gets a dictionary
def WriteDictionary(dict):
	return str(dict)