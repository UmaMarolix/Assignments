import math

def jumpsearch(arr,x,n):
    arr.sort()   #sorting the arr
    print(arr)

    prev=0  
    # finding the block size to be jumped
    step =int(math.sqrt(n))

# finding the block where element is present
    while arr[int(min(step,n)-1)]<x:
        prev=step
        step +=(int(math.sqrt(n)))

        if prev>=n:
            return None
        
# Doing a linear search for x in
# # block begining with prev
    while arr[int(prev)]<x:
        prev +=1
#if we reached the end of arr but element is not present
        if arr[int(prev)]==min(step,n):
            return None
#element is found       
        if arr[int(prev)]==x:
            return prev
        else:
            return None

arr=[17,90,44,76,89,100,110] 
x=89  #element to be search
n=len(arr)  

print("The position of searching element is",jumpsearch(arr,x,n))



