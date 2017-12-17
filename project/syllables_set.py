import sys
import re

w = open('rutul.tsv', 'r')
words = ''
for line in w.readlines():
	line = line.strip()
	if '#' in line:
		continue
	row = line.split('\t')
	words = words + row[2] + '\n'

syllables_list = '# Syllable\tWord'
syllables = input('Write the syllables. For more than one, separate them by comma: ')
syllables = syllables.split(',')
for syllable in syllables:
	syllable = syllable.strip()
	m = re.findall(r'[а-я1]*%s[^ьъ1][а-я1]*' % syllable, words)
	if not m:
		continue
	for list_form in m:
		syllables_list = syllables_list + '\n' + syllable + '\t' + list_form
print(syllables_list, file=open("syllables.txt", "w"))
