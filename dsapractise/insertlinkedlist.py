# Creation of linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class slinkedlist:
    def __init__(self):
        self.head=None

    def display(self):

        if self.head is None:
            print("linked list is Empty")
        else:
            temp=self.head  
            while temp:
               print(temp.data,"-----",end="")
               temp=temp.next 
    def insertstart(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode


L=slinkedlist()  #creation of empty linked list

n=Node(20)
L.head=n

n1=Node(22)
L.head.next=n1 

n2=Node(221)
n1.next=n2

L.insertstart(1111)

L.display()      # function to display





