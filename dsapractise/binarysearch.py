# Binary search
def binary_search(arr,x):
    arr.sort()
    print(arr)

    left,right=0,len(arr)-1


    while left<=right:
        mid=(left+right)//2

        if arr[mid]==x:
            return mid
        
        elif arr[mid]>x:
            right=left-1
        elif arr[mid]<x:
            left=right+1

    else:
        return None        

arr=[5,8,3,7,10,33]
x=7   # element to search in arr
result=binary_search(arr,x)

if result != -1:
    print("Element is present at index ",str(result))
else:
    print("Element is Not found")    

    