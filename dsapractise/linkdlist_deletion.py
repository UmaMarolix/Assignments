#linked list deletion at the starting ending and inbetween
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def ___init__(self):
        self.head=None   


    def insert_start(self,data):
        nd=Node(data)
        nd.next=self.head
        self.head=nd

    def del_start(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def del_end(self):
        previous=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            previous=previous.next
               
        previous.next=None   

    def del_inbetween(self,position):
        previous=self.head
        temp=self.head.next
        for i in range(1,position-1):
            temp=temp.next
            previous=previous.next
               
        previous.next=temp.next  
    




        

             

    def display(self):
        if self.head is None:
            print("empty linkedlist")
        else:
            temp=self.head
            while temp:
                print(temp.data) 
                temp=temp.next   


L=linkedlist()
n=Node(2) 
L.head=n

n1=Node(3)
n.next=n1

n2=Node(22)
n1.next=n2

n3=Node(66)
n2.next=n3

L.insert_start(1)
L.del_start()
L.del_end()
L.del_inbetween(2)

L.display()             
