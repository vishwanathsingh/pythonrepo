#!/bin/python

def maxProfitBoarding():
		firstLine=raw_input().split(' ')
		bundle=int(firstLine[1])
		arrSize=int(firstLine[0])
		arr=[0 for x in range(0,arrSize)]
		for i in range(0,arrSize):
			arr[i]=int(raw_input()) 
		
		index=-1
		maximum=sum=0
		
		print "input array is ",arr
		
		for i in range(0,bundle):
			if(i<=arrSize):
				sum+=arr[i]
			else:
				break
		
		
		for x in range(1,arrSize):
			if(x+bundle <= arrSize):
				tempSum=sum-arr[x-1]+arr[x+bundle-1]
				arr[x-1]=sum
				sum=tempSum
			
			else:
					arr[x-1]=sum
					arrSize=x
				
		
		
				
				
		
		print "input array is",arr
		
		for i in range(0,bundle):
			for x in range(i+bundle+1,arrSize,bundle+1):
				arr[i]+= arr[x]
		
		print "input array is",arr
		
		for x in range(0,arrSize):
			if (maximum < arr[x]):
				maximum=arr[x]
				
		
		print maximum
				

if(__name__ == "__main__"):
	maxProfitBoarding()		
