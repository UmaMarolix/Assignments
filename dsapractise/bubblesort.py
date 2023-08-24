n=int(input("Enter the size of array : "))
arr=[]
for i in range(n):
    val=int(input("Enter the number to add in the array: "))
    arr.append(val)    
print(arr)

def bubblesort(arr, n):
    for i in range(n):
        print("i is",i)
        print("arr[i] : ",arr[i])
        
        for j in range(0, n-i-1):
            print("array:",arr)
            print("j is", j)
            print("arr[j] : ", arr[j])
            print("arr[j+1] : ", arr[j+1])
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr
    
print(bubblesort(arr,n))           
