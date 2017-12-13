import sys

sent_id = 1

# sys.stdout = open('output.txt',  'wt')

# print("Index\tSurface form\tLemma\tUPOS\tXPOS\tMorph. features\tHead\tRelation\tSecondary dependencies\tMiscellaneous")

for line in sys.stdin.readlines():
	if line != '\n':
		line = line.strip()
		print('# sent_id = %d' % (sent_id))
		print('# text = %s' % (line))
		for p in '?!,.;:)\"':
			line = line.replace(p, ' ' + p)
		for p in '(\"':
			line =  line.replace(p, p + ' ')
		tokens = line.split(' ')
		token_id = 1
		for token in tokens:
			if token.strip() == '':
				continue
			print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' %(token_id, token))
			token_id = token_id + 1
		sent_id = sent_id + 1
		print('')