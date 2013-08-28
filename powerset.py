from pprint import *
a = [1,2,3,4]
total = [[]]
for i in a:
	for value in total[:]:
		total.append(value+ [i])
pprint(total)
