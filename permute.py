import sys
import pprint
total=0
things = []
def perm(pref, rest):
	i=len(rest)
	if(i==0):
		print(pref + " " + rest)
		global total, things
		total+=1
		#things.append(pref)
		pass
	j=0
	for a in rest:
		j+=1
		perm(pref+a, rest[0:j-1]+rest[j:i])
	
def main():
	i =0
	for a in sys.argv:
		if i==1:
			perm("", a)
		i+=1
	global total,things
	#pprint.pprint(things, indent=2, width = 2)
	#print(things)
	
	print("Total combos: "+str(total))
	
main()