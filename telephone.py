import sys
def main():
	str1 = input("Enter Number:")
	d = {}
	for line in open("numbers.txt"):
		a,b = line.split()
		d[a] = b
	for c in str1:
		if(c.upper() in d):
			sys.stdout.write(d[c.upper()])
main()