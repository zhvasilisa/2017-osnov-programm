import sys

wt = {}
freq_tag = 0

# Read the model

model = open('model.tsv', 'r')
for line in model.readlines():
	line = line.strip('\n')
	row = line.split('\t')
	if '#' not in line:
		prob = float(row[0])
		tag = row[2]
		form = row[3]

# Count the most frequent tag

		if form ==  '_':
			if prob > freq_tag:
				freq_tag = prob
				most_freq_tag = tag

# 	Make a dictionary from the model

		wt[form] = {}
		wt[form][tag] = prob

# 	Read the input

for line in sys.stdin.readlines():
	if '\t' not in line:
		print(line)
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue

# 	Add the tags

	for form in wt:

# 	Add tags to the words from the same as in the model

		if row[1] == form:
			tag_count = 0
			for tag in wt[form]:
				if wt[form][tag] > tag_count:
					tag_count = wt[form][tag]
					row[3] = tag
					print('\t'.join(row))

# 	Add tags to the words not the same as in the model

	if row[3]	== '_':
		row[3] = most_freq_tag
		print('\t'.join(row))
