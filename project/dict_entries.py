import sys
import re

s =  open('jamalov.txt', 'r')
print('# Word', file=open("entries.txt", "w"))
for line in s.readlines():
	line = line.strip()
	if line == '':
		continue
	m = re.search(r'^[А-Я\'1-]+', line)
	if not m:
		continue
	entry = m.group()
	if len(entry) > 1:
		entry = entry.replace('\'', '').lower().replace('аь', 'а1')
		print('%s'  % (entry), file=open("entries.txt", "a"))