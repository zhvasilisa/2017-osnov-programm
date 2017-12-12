import sys

m = {}
t = {}
total = 0

for line in sys.stdin.readlines():
	if line[0] == '':
		continue
	if '\t' not in line:
		continue
	row = line.split('\t')
	
	form = row[1]
	tag = row[3]
	if tag == "_":
		continue
	total = total + 1

	if form not in m:
		m[form] = {}
	if tag not in m[form]:
		m[form][tag] = 0
	m[form][tag] = m[form][tag] + 1

	if tag not in t:
		t[tag] = 0
	t[tag] = t[tag] + 1

print(t)
print(total)

print('# P\tcount\ttag\tform', file=open("output.txt", "w"))

for tag in t:
	tag_prob = t[tag]/total
	print('%.2f\t%d\t%s\t_'  % (tag_prob, t[tag], tag), file=open("output.txt", "a"))

for form in m:
	form_freq = 0
	for tag in m[form]:
		form_freq = form_freq + m[form][tag]
	for tag in m[form]:	
		pair_prob = m[form][tag]/form_freq
		print('%.2f\t%d\t%s\t%s'  % (pair_prob, m[form][tag], tag, form), file=open("output.txt", "a"))
	
