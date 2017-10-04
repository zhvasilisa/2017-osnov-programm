import sys

for line in sys.stdin.readlines():
	print(line.replace('. ', '.\n'))