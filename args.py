import sys
from collections import defaultdict
def main():
	i =0
	words = defaultdict(list)
	for a in sys.argv:
		if i!=0:
			j = 0
			for c in a:
				j+=ord(c)
			words[j].append(a)
			#print(words)
		i+=1
	for key in words:
		for thing in words[key]:
			sys.stdout.write(thing + ' ')
		print()
main()