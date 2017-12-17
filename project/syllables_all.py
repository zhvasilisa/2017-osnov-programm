import sys
import re

vowels = ['а', 'а1', 'о', 'и', 'ы', 'е']
sounds = open('sounds.txt', 'r')
consonants = ''
for line in sounds.readlines():
	line = line.strip()
	if '#' in line:
		continue
	row = line.split('\t')
	consonants = consonants + ',' + row[0]

consonants = consonants.strip(',').split(',')

w = open('rutul.tsv', 'r')
output = '# Syllable\tWord'
for line in w.readlines():
	line = line.strip()
	if '#' in line:
		continue
	row = line.split('\t')
	word = row[2]
	for vowel in vowels:
		for consonant in consonants:
			m = re.findall(r'%s%s[^%s1ьъ][1ьъ]?' % (consonant, vowel, vowel), word)
			if not m:
				continue
			for syllable in m:
				output = output + '\n' + syllable + '\t' + word
	
print(output, file=open("syllables.txt", "w"))