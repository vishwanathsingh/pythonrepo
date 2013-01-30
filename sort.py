#!/bin/python
import math

def sort(arr):
	length=len(arr)
	if (length<=1):
		return
	arr_A=[0 for x in range(0,int(math.floor((float(length)/2))))]
	arr_B=[0 for x in range(0,int(math.ceil((float(length)/2))))]
	sortedArr=[0 for x in range(0,len(arr))]
	for i in range (0,len(arr_A)):
	#	print "i is",i
		arr_A[i]=arr[i]
	for i in range (0,len(arr_B)):
		arr_B[i]=arr[length/2 + i]

	print "array A is",arr_A
	print "array B is",arr_B	
	sort(arr_A)
	sort(arr_B)
	
	#print "sorted array A is",sorted_A
	#print "sorted array B is",sorted_B
	merge(arr_A,arr_B,arr)
	print arr

def merge(A,B,C):
	i=a=b=0;
	print "received array A is",A
	print "received array B is",B
	print "received array C is",C
	while (a<len(A) and b<len(B)):
		if( A[a] < B[b]):
			C[i]=A[a]
			i+=1
			a+=1
		else:
			C[i]=B[b]
			i+=1
			b+=1
	
	if (a == len(A)):
		for k in range(b,len(B)):
			C[i]=B[k]
			i+=1
			k+=1
			
	else:
		for k in range(a,len(A)):
			C[i]=A[k]
			i+=1
			k+=1
