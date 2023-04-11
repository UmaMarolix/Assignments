# linear data structure
def linear_search(a,key,size):
    flag=0  # index place of number from where it should search
    for i in range(size):
        if a[i]==key:
            flag=1  # it means the number which we are searching has found
            pos=i+1 #i means in which index we got the searching number and +1 is get the position bcoz index start from zero but we want to get the number to start from 1...like i(index)=2 +1 =3 rd position
            break
    if flag==1:
            print("Number found at", pos,"position")
    else:
            print("Number is not found")    




a=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the number to add in the list: "))
    a.append(val)
key=int(input("Enter the number to search in the list:"))
linear_search(a,key,size)