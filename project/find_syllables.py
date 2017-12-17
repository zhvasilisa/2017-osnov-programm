import sys
import re

final = '#Syllable\tList Frequency\tDict Frequency\tDict Forms'

# Extract all syllables with the frequencies into the dictionary syl (DONE)

syllables = open('syllables.txt', 'r')
syl = {}
for line in syllables.readlines():
	line = line.strip()
	if '#' in line:
		continue
	row = line.split('\t')
	if row[0] not in syl:
		syl[row[0]] = 0
	syl[row[0]] = syl[row[0]] + 1

# Look for syllables in the entries from the dictionary (MAYBE EXCLUDE THE LIST OF WORDS)

entries = open('entries.txt', 'r').read()
dict_freq = 0
for syllable in syl:
	m = re.findall(r'[а-я1-]*%s[^ьъ1][а-я1-]*' % syllable, entries)
	if not m:
		final = final + '\n' + syllable + '\t' + str(syl[syllable]) + '\t' + str(0) + '\t' + '_'
		continue
	dict_forms = ', '.join(m).replace('\n', '')
	dict_freq = len(m)
	final = final + '\n' + syllable + '\t' + str(syl[syllable]) + '\t' + str(dict_freq)+ '\t' + dict_forms
		
print(final, file=open("frequencies.tsv", "w"))
