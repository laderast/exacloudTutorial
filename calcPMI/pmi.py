"""
Pointwise Mutual Information

Ryan Swan
2015-10-23

This script takes a filename as an argument. The file must contain tweets from the
twitter sentiment analysis data set housed at http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip

The script processes the input file and produces an output file with .pmioutput added to the original name.
The output file contains a dictionary of values containing:

for each word:
	count of occurrences
	count of cooccurrence with term 1
	count of cooccurrence with term 2
under the __totalcorpus key:
	count of all tweets analyzed
	count of occurrences of term 1
	count of occurrences of term 2

example:
	call:		python pmi.py samplecorpus.txt
	returns: 	samplecorpus.txt.pmioutput
"""

# libraries
import math		# math for log function
import re		# re for string operations
import string	# string for filtering
import sys		# sys for accepting command line arguments
import csv		# csv to open file
import cPickle	# for saving output

# Parameters
woi1 = "at"	# first word to compare 2grams
woi2 = "the"	# second word to compare 2grams

# load data
filename = sys.argv[1]
#filename = "sample.csv"
fh = open(filename, "r")

# Initialize dictionaries and counters
word_dict	= {}			# this dictionary contains entry with each new word as key and values for:
							#    1. count: number of times that word appears in a tweet
							#	 2. cooccurrence1: number of times word appears cooccurrent with woi1
							#	 3. cooccurrence2: number of times word appears cooccurrent with woi2
woi1_ct 	= float()
woi2_ct 	= float(0)
both_ct		= float(0)
tweet_ct 	= float(0)

# Create punctuation filter
pfilt = string.punctuation
pfilt = pfilt.replace("#","")

# Create regular expression for matching usernames


# Loop through file
reader = csv.reader(fh)

for line in reader:
	tweet = line[5]		# Tweet text is contained at the fifth index as string
	tweet = tweet.lower().split(" ") # Make lowercase and split on whitespace
	# regular expression filter to exclude usernames goes here
	# Remove punctuation
	tweet = [i.translate(string.maketrans("",""),pfilt) for i in tweet]
	# Remove duplicates
	tweet = set(tweet)
	# add words to dictionary and perform cooccurrence counts
	for word in tweet:
		if word == woi1 or word == woi2:
			pass
		else:
			if word in word_dict:
				pass
			else:
				word_dict[word] = {"count":float(0),"cooccurrence1":float(0),"cooccurrence2":float(0)}
			word_dict[word]["count"] += 1
			if woi1 in tweet:
				word_dict[word]["cooccurrence1"] += 1
			if woi2 in tweet:
				word_dict[word]["cooccurrence2"] += 1
	# Perform counts
	if woi1 in tweet:
		woi1_ct += 1
	if woi2 in tweet:
		woi2_ct += 1
	tweet_ct += 1

fh.close()

# Create output dictionary
word_dict["__totalcorpus"] = {"count":tweet_ct,"term1_ct":woi1_ct,"term2_ct":woi2_ct}

# Write output dictionary to file
with open(filename + ".pmioutput","w") as fh:
	cPickle.dump(word_dict,fh)
