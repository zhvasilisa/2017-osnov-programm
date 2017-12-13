import sys

# Make a dictionary from the list of letters
lettersdict = {}
tr = open('letters.txt', 'r')
for line in tr.readlines():
	line = line.strip('\n')
	(l, c) = line.split('\t')
	lettersdict[l] = c

for line in sys.stdin.readlines():
	line = line.strip()
	if '\t' not in line:
		print(line)
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	form = row[1]
	newform = '#' + form
	row[9] = 'Translit='
	for l in lettersdict:
		newform = newform.replace(l, lettersdict[l])
	row[9] = row[9] + newform.strip('#')
	print('\t'.join(row))

	