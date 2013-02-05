#!/bin/python


def maxProfit():
		firstLine=raw_input().split(' ')
                bundle=int(firstLine[1])
                arrSize=int(firstLine[0])
                arr=[0 for x in range(0,arrSize)]
                for i in range(0,arrSize):
                    arr[i]=int(raw_input())
                indexArr=[0 for x in range(0,arrSize)]
                profitArr=[0 for x in range(0,arrSize)]
                profitArr[0]=arr[0]  #base case for dp recurrence
                indexArr[0]=1
                if(bundle > 1):   #bundle size less than 1 doesn't make much sense
                    profitArr[1]=profitArr[0]+arr[1]
                    indexArr[1]=2
                
                #profitArr[i] stores the profit till i'th billboard 
                for i in range(2,arrSize):
                    if(indexArr[i-1]!=bundle):
                        profitArr[i]=profitArr[i-1]+arr[i]
                        indexArr[i]=indexArr[i-1]+1
                    else:
                        if((arr[i-bundle] < arr[i]) and ((profitArr[i-2] + arr[i] < profitArr[i-1]) or bundle==2)):    #remove first element in bunde and add this
                            profitArr[i]=profitArr[i-1]-arr[i-bundle]+arr[i]
                            x=i-bundle
                            while(x<=i-1):
                                indexArr[x]-=1
                                x+=1

                            indexArr[i]=bundle
                            continue

                        if(bundle!=2 and profitArr[i-2] + arr[i] > profitArr[i-1]):                 #remove last element of bundle, bundle size of k-1
                            profitArr[i]=profitArr[i-2]+arr[i]
                            indexArr[i]=1
                            indexArr[i-1]=0
                            continue
                        
                        profitArr[i]=profitArr[i-1]
                            
                        
                
                print "profitArr=",profitArr
                print "indexArr=",indexArr
                print profitArr[arrSize-1]

                
                
if (__name__ == '__main__'):
    maxProfit()
