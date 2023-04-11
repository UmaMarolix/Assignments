# Creation of linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class slinkedlist:
    def __init__(self):
        self.head=None

    
    def insert_begining(self,newdata):
        newnode=Node(newdata) 
        newnode.next=self.head
        self.head=newnode

    def insert_end(self,newdata):
        newnode=Node(newdata)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        

    def insert_position(self,position,newdata):
        newnode=Node(newdata)
        temp=self.head
        for i in range(position-1):
            temp=temp.next
        newnode.newdata=newdata
        newnode.next=temp.next 
        temp.next=newnode





    def display(self):

        if self.head is None:
            print("linked list is Empty")
        else:
            temp=self.head  
            while temp:
               print(temp.data,"-----",end="")
               temp=temp.next 
    
            


           


L=slinkedlist()  #creation of empty linked list

n=Node(20)
L.head=n

n1=Node(22)
L.head.next=n1

n2=Node(221)
n1.next=n2

L.insert_begining(1111)

L.insert_end(123)
L.insert_position(2,33)

L.display()      # function to display
