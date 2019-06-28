################
# Ephycis      #
# Jun 28, 2019 #
################

import random

# Default values
singleAmount = 0
doubleAmount = 0
tripleAmount = 0

# Onset, Nucleus, Coda
### PUT YOUR OWN SPACES IN ###
ons = ['m', 'n', 'ng', 'p', 't', 'k', 'f', 'th', 's', 'sh', 'x', 'h', 'w', 'j', 'l', 'r']
nuc = ['i', 'e', 'a', 'o', 'u']
cod = ['m', 'n', 'ng', '', '', '']

# Generates a segment of the sylable
def Gen(part):

	"""
	# The "part" is the same as the ons/nuc/cod
	return part[random.randint(0, len(part)-1)]
	"""

	# I tried it where part was in the place of ons/nuc/cod
	# but it glitched and this is just simpler
	if part == "ons":
		return ons[random.randint(0, len(ons)-1)]
	elif part == "nuc":
		return nuc[random.randint(0, len(nuc)-1)]
	elif part == "cod":
		return cod[random.randint(0, len(cod)-1)]
	else:
		print("GEN ERROR")

# Creates the whole word
def Cre(sylables):

	# 1-2-3 for how many sylables you want
	if sylables == 1:
		print(f"/{Gen('ons')}{Gen('nuc')}{Gen('cod')}/")
	elif sylables == 2:
		print(f"/{Gen('ons')}{Gen('nuc')}{Gen('cod')}{Gen('ons')}{Gen('nuc')}{Gen('cod')}/")
	elif sylables == 3:
		print(f"/{Gen('ons')}{Gen('nuc')}{Gen('cod')}{Gen('ons')}{Gen('nuc')}{Gen('cod')}{Gen('ons')}{Gen('nuc')}{Gen('cod')}/")
	else:
		print("CRE ERROR")

# Main
def Main():

	# How many of each you want
	singleAmount = input("How many 1 sylable words would you like to generate? ")
	doubleAmount = input("How many 2 sylable words would you like to generate? ")
	tripleAmount = input("How many 3 sylable words would you like to generate? ")

	# Prevents letters
	try:
		singleAmount = int(singleAmount)
	except ValueError:
		singleAmount = 0

	try:
		doubleAmount = int(doubleAmount)
	except ValueError:
		doubleAmount = 0

	try:
		tripleAmount = int(tripleAmount)
	except ValueError:
		tripleAmount = 0

	# Prevents negative numbers
	if singleAmount < 0:
		singleAmount = 0
	
	if doubleAmount < 0:
		doubleAmount = 0

	if tripleAmount < 0:
		tripleAmount = 0

	# Break
	print()

	for i in range(singleAmount):
		Cre(1)
	for i in range(doubleAmount):
		Cre(2)
	for i in range(tripleAmount):
		Cre(3)

	# Break
	print()

	# Go again
	ans = input("Again? (y/n)")

	# Break
	print()

	# Visual break of the sessions
	print("~O~")

	# Break
	print()

	# If you mistype, it's a no
	try:
		ans = ans.lower()
	except:
		ans = "n"

	if ans == "y":
		Main()
	elif ans == "n":
		print("bye")
	else:
		print("bye")

	

#----------------------------------------------#

# The begining of the script 

# Intro
print("Welcome to the ConLang Word Generator!")

# These are breaks
print()

Main()