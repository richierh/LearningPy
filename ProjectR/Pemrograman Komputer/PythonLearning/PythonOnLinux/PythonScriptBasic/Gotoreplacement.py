def getFloat(prompt):
	result = None # this will be the valid number, right now it's not
	while result == None: # until this value is set, they don't leave
		try:
			result = float(input(prompt))
			# if made it this far, result has a new value
		except:
			# if they're here, result never got loaded with a value
			print ("You must enter a number!")
	return result

# we don't cave about the values in the function
# we only care that passes back a float
kcel = getFloat("\nWhat is the degrees in Celsius? ")
# since kcel is in scope, we can use it here
print ("\n"  ,kcel, "degrees Celsius is", kcel + 273, "degrees Kelvin.\n\n")

