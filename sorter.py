# Nick Robertson
# https://github.com/nar213/SortingExamples

import random
import os

print "  ____             _   _                  _    _                  _ _   _                    "
print " / ___|  ___  _ __| |_(_)_ __   __ _     / \  | | __ _  ___  _ __(_) |_| |__  _ __ ___  ___  "
print " \___ \ / _ \| '__| __| | '_ \ / _` |   / _ \ | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \/ __| "
print "  ___) | (_) | |  | |_| | | | | (_| |  / ___ \| | (_| | (_) | |  | | |_| | | | | | | | \__ \ "
print " |____/ \___/|_|   \__|_|_| |_|\__, | /_/   \_\_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|___/ "
print "                               |___/             |___/                                       "
print "Code by Nick Robertson"
print "https://github.com/nar213/SortingExamples"

inputchoice =0
random_items = []
while inputchoice == 0 :

	print "\nInput Source"
	print " Option 1: 100 Random Integers between 0 and 1000"
	print " Option 2: Text File (Numbers seperated by spaces)"
	print " Option 3: Select Range and Size of Random Integer List"

	inputchoice = input()

	#100 RANDOM INTEGERS
	if inputchoice == 1:
		print "\n100 Random Integers between 0 and 1000 Selected"
		random_items = [random.randint(0, 1000) for i in range(100)]

	#TEXT INPUT
	elif inputchoice == 2:
		print "\nText File Input Selected (NB Ensure each number is seperated by a line)"
		print "\nInput File Name"
		infile = raw_input()
		while os.path.isfile(infile) != True:
			print "\nFile not Found"
			print "Re-Input File Name"
			infile = raw_input()
		thisfile = open(infile)
		for eachline in thisfile:
			random_items.append(int(eachline))
		thisfile.close()

	#RANDOM RANGE
	elif inputchoice == 3:
		print "\nUser Defined Random Numbers Selected"
		print "\nSelect Lower Bound "
		lowerbound = input()
		print "\nSelect Upper Bound "
		upperbound = input()
		while upperbound < lowerbound:
			print "\nThe Upper Bound must be greater than or equal to Lower Bound"
			upperbound = input()
		print "\nSize of the List "
		listsize = input()
		while listsize < 0:
			print "\nThe Size of the List must be greater than 0"
			upperbound = input()
		random_items = [random.randint(lowerbound, upperbound) for i in range(listsize)]
	else:
		print "\nInvalid Input Choice"
		inputchoice = 0

outputchoice = 0
while outputchoice == 0 :

	print "\nOutput Destination"
	print " Option 1: Print to Screen"
	print " Option 2: Write to File"

	outputchoice = input()

	if outputchoice ==  1:
		print "\nPrint to Screen Selected"
	elif outputchoice == 2:
		print "\nWrite to File Selected"
		print "\nEnter File Name"
		outfile = raw_input()
	else:
		print "\nInvalid Output Choice"
		outputchoice = 0 

algchoice = 0
while algchoice ==0:

	print "\nSelect Sorting Algorithm"
	print " Option 1: Bubble Sort"
	print " Option 2: Insertion Sort"
	print " Option 3: Merge Sort"
	print " Option 4: Quick Sort"
	print " Option 5: Heap Sort"

	algchoice = input()

	if algchoice == 1:
		print "\nBubble Sort Selected"
	elif algchoice == 2:
		print "\nInsertion Sort Selected"
	elif algchoice == 3:
		print "\nMerge Sort Selected"
	elif algchoice == 4:
		print "\nQuick Sort Selected"
	elif algchoice == 5:
		print "\nHeap Sort Selected"
	else:
		print "\nInvalid Algorithm Choice"
		algchoice=0

#TODO Implement Functions

comparisons = 0
accesses =0

print '\nUnsorted List:\n ',random_items
print '\nSorted List:\n ',random_items #Change to Sorted List on Completion
print '\nNumber of Comparisons ', comparisons
print 'Number of Array Accesses: ', accesses
print 'Size of List: ', len(random_items)
if outputchoice == 2:
	thisfile = open(outfile, 'w')
	for element in random_items: #Change to Sorted List on Completion
		thisfile.write(str(element))
		thisfile.write("\n")
	thisfile.close()
	print '\nList written to File\n'

# Comparisons Information
# Array Accesses Information
# Sorted List, Make Optional