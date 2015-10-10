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

#CLASSES

class counterobject:
	counter = 0
	def __init__(self):
		self.counter = 0
	def inc(self):
		self.counter = self.counter + 1
	def val(self):
		return self.counter

#FUNCTION DEFINITIONS

def bubblesort(unsorted, comparisons, swaps):
	sortedlist = []

	for element in unsorted:
		sortedlist.append(element)	#Maintains unsorted array

	for number in range(len(sortedlist)-1, 0 ,-1):	
		for i in range(number):
			comparisons.inc()
			if sortedlist[i]>sortedlist[i+1]:
				swaps.inc()
				temp = sortedlist[i]
				sortedlist[i] = sortedlist[i+1]
				sortedlist[i+1] = temp
	print "Bubble Sort Complete"
	return sortedlist

def insertsort(unsorted, comparisons, swaps):
	print "Insertion Sort Complete"

def mergesort(unsorted, comparisons, swaps):
	print "Merge Sort Complete"

def quicksort(unsorted, comparisons, swaps):
	print "Quick Sort Complete"

def heapsort(unsorted, comparisons, swaps):
	print "Heap Sort Complete"

def selectionsort(unsorted, comparisons, swaps):
	print "Selection Sort Complete"

def timsort(unsorted, comparisons, swaps):
	print "TimSort Sort Complete"


comparisons = counterobject()
swaps = counterobject()

#USER INTERFACE

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
	print " Option 6: Selection Sort"
	print " Option 7: TimSort"

	algchoice = input()

	if algchoice == 1:
		print "\nBubble Sort Selected"
		sorted_items = bubblesort(random_items,comparisons, swaps)
	elif algchoice == 2:
		print "\nInsertion Sort Selected"
		insertsort(random_items,comparisons, swaps)
	elif algchoice == 3:
		print "\nMerge Sort Selected"
		mergesort(random_items,comparisons, swaps)
	elif algchoice == 4:
		print "\nQuick Sort Selected"
		quicksort(random_items,comparisons, swaps)
	elif algchoice == 5:
		print "\nHeap Sort Selected"
		heapsort(random_items,comparisons, swaps)
	elif algchoice == 6:
		print "\nSelection Sort Selected"
		selectionsort(random_items,comparisons, swaps)
	elif algchoice == 7:
		print "\nTimSort Selected"
		timsort(random_items,comparisons, swaps)
	else:
		print "\nInvalid Algorithm Choice"
		algchoice=0





print '\nUnsorted List:\n ',random_items
print '\nSorted List:\n ',sorted_items #Change to Sorted List on Completion
print '\nSize of List: ',len(random_items)
print '\nNumber of Comparisons: ',comparisons.val()
print 'Number of Swaps: ',swaps.val()

if outputchoice == 2:
	thisfile = open(outfile, 'w')
	for element in random_items: #Change to Sorted List on Completion
		thisfile.write(str(element))
		thisfile.write("\n")
	thisfile.close()
	print '\nList written to File\n'