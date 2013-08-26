import sys
from random import *; from pprint import *
def merge(l1, l2):
	result = []
	#print("merging: " + str(l1+l2))
	i1,i2=0,0
	while i1<len(l1) and i2<len(l2):
		if l1[i1] > l2[i2]:
			result.append(l2[i2])
			i2+=1
		else:
			result.append(l1[i1])
			i1+=1
	if(i1<len(l1)):
		result.extend(l1[i1:])
	if(i2<len(l2)):
		result.extend(l2[i2:])
	return result		
def ms(d):
	if(len(d)<=1):
		return d
	mid = round(len(d)/2)
	#print("merge of "+ str(d[:mid]) + " " + str(d[mid:]))
	return merge(ms(d[:mid]),ms(d[mid:]))
def qs(d):

	if(len(d)<=1):
		return d
	pivot = d[randint(0,len(d)-1)]
	less = []; more = []; curr = []
	for x in range(len(d)):
		if(d[x]<pivot):
			less.append(d[x])
		else:
			if(d[x]>pivot):
				more.append(d[x])
			if(d[x]==pivot):
				curr.append(d[x])
	return qs(less)+curr+qs(more)
def main():
	d = []
	for line in open("number.txt"):
		d.append(int(line.split()[0]))
	print(qs(d))
	print(ms(d))
main()