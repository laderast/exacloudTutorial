"""
Script looks for files with .pmioutput flag and combines those dictionaries into a 
	single dictionary of values. This dictionary is output as 'totalpmioutput.csv' in csv format.
"""

import os
import cPickle
import math
import re

def calcPMI(word_count,woi_count,total_count,cooccurrence_count):
	"""calculates pointwise mutual information for each word with a given word of interest"""
	word_count = float(word_count)
	woi_count = float(woi_count)
	total_count = float(total_count)
	cooccurrence_count = float(cooccurrence_count)
	pmi = math.log((cooccurrence_count/word_count)/((woi_count/total_count)*(word_count/total_count)))
	return pmi

def stitchDicts(dict1,filename):
	"""
	Combines two dictionaries and outputs a dictionary that combines their counts
	dict1 = a dictionary object (pass an empty dictionary on first iteration)
	filename = the filename of a .pmioutput file to combine with the basedict
	"""
	# Base case for first iteration when dictionary object will be empty
	dict2 = cPickle.load(open(filename,"r"))
	if len(dict1) == 0:
		dict1 = dict2
	else:
		for k in dict2.keys():
			if k in dict1:
				for k2 in dict2[k]:
					dict1[k][k2] += dict2[k][k2]
			else:
				dict1[k] = dict2[k]
	return dict1

# Get list of files with .pmioutput file extension
file_list = os.listdir(os.getcwd())
pmioutput_list = []
for f in file_list:
	if re.search(r"\.pmioutput",f):
		pmioutput_list.append(f)

# Combine files into one dictionary
word_dict = {}
for d in pmioutput_list:
	word_dict = stitchDicts(word_dict,d)

# Calculate pmi measures
pmi_dict = {}
for word in word_dict:
	if word != "__totalcorpus":
		pmi_dict[word] = {"woi1":0,"woi2":0}
		if word_dict[word]["cooccurrence1"] > 0:
			pmi_dict[word]["woi1"] = calcPMI(word_dict[word]["count"],word_dict["__totalcorpus"]["term1_ct"],word_dict["__totalcorpus"]["count"],word_dict[word]["cooccurrence1"])
		if word_dict[word]["cooccurrence2"] > 0:
			pmi_dict[word]["woi2"] = calcPMI(word_dict[word]["count"],word_dict["__totalcorpus"]["term2_ct"],word_dict["__totalcorpus"]["count"],word_dict[word]["cooccurrence2"])

# Write out total output as csv
with open("totalpmioutput.csv","w") as fh:
	fh.write("word,pmi_term1_w_word,pmi_term2_w_word\n")
	for word in pmi_dict:
		fh.write(str(word) + "," + str(pmi_dict[word]["woi1"]) + "," + str(pmi_dict[word]["woi2"]) + "\n")

