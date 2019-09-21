# Linked List is a data structure used for storing collections of data.
# A linked list is a list where each item is in a separate node. Each node holds two pieces
# of information the data and a reference link to the next node.
# Linked List has two main advantages over a python list 
# (1) They are dynamic
# (2) Insertion and deletion is more efficient
# Main disadvantage is that indexing takes O(n) 


# Singly Linked Lists: is a collection that form a linear sequence

# Node class and a singly link list class.
# Node class
class Node:
    node_count = 0
    def __init__(self, data ):
        self.data = data  
        self.next = None 
        Node.node_count += 1 
  
# Linked List class
class LinkedList:
    
    def __init__(self): 
        self.head = None
        self.count = 0


    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head=new_node  
        else:
            new_node.next=self.head
            self.head=new_node            
       

    def insertAfter(self, prev_node, new_data):
        x=self.head
        while (x != None):
            if x.data == prev_node:
                break 
            x=x.next 
        if x is None: 
            print("prev_node not found")
        else:
            new_node = Node(new_data)
            new_node.next = x.next
            x.next=new_node
            return f"Next of previous Node '{prev_node}' is {x.next.data}"
             


    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
  
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):   
            last = last.next
        last.next = new_node


    def deleteFromBeginning(self): 
        if Node.node_count == 0: 
            print ("The list is empty") 
        else: 
            self.head = self.head.next 
            Node.node_count -= 1
            print("\nNext of NewHead:", self.head.next.data)


    def DeleteAtEnd(self):
        if self.head is None:
            print("The list is empty")
        else:
            y=self.head
            z=y.next
            while (z.next is not None):
                y=y.next
                z=z.next
                print("z:", z.data)
            y.next= None
            Node.node_count -= 1


    def DeleteAtMiddle(self,value):
        x=self.head
        if x!=None:
            while x!=None:
                if x.data==value: 
                    break
                y=x
                print("y:1", y.data)    
                x=x.next 
                print("x:", x.data)
            if x==None: 
                return 
            y.next=x.next
            print("y:", y.data)
            print("y:", y.next.data)
            x=None
            Node.node_count -= 1


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

# Comment out the below codes and run one by one 

llist = LinkedList()
llist.insertAtBeginning("B")
llist.insertAtBeginning("A")

print(llist.insertAfter("B", "C"))
print(llist.insertAfter("C", "D"))

llist.insertAtEnd("E")
llist.insertAtEnd("F")

llist.deleteFromBeginning()
llist.DeleteAtEnd()
llist.DeleteAtMiddle("D")

print("\nNodes")
llist.printList()
print("Count of Nodes", Node.node_count)





# Node class and a Doubly link list class.
# Node class
class Node:
    node_count = 0
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.previous = None
        Node.node_count += 1
        
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.previous = new_node
            self.head = new_node
            return f"\n I'm '{new_node.data}', My next is {new_node.next.data}"


    def insertAfter(self, prev_data, new_data):
        new_node = Node(new_data)
        x = self.head
        while x.data != prev_data:
            x = x.next
        new_node.next = x.next
        x.next.previous = new_node
        x.next = new_node
        new_node.previous = x
        print(f"\nNew Node '{new_data}', previous is '{new_node.previous.data}' and it's Next is '{new_node.next.data}'.")
    
    
    def insertAtEnd(self, value):        
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node


    def deleteAtFirst(self):
        self.head = self.head.next
        self.head.previous = None
        Node.node_count -= 1


    def deleteByValue(self, value):        
        if self.head is None:
            raise Exception("LIST IS EMPTY")
        else:
            x = self.head
            while x.data != value and x != None:
                x = x.next
            n = x.next
            x = x.previous
            n.prev = x
            x.next = n
            del(x)
            Node.node_count -= 1
    
    def deleteAtLast(self):
        self.tail = self.tail.previous
        self.tail.next = None
        Node.node_count -= 1


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

llist = DLL()
print(llist.insertAtBeginning("E"))
print(llist.insertAtBeginning("D"))
print(llist.insertAtBeginning("C"))
print(llist.insertAtBeginning("B"))
print(llist.insertAtBeginning("A"))

print(llist.insertAfter("D", "K"))

llist.insertAtEnd("Z")

llist.deleteAtFirst()

llist.deleteByValue("C")

llist.deleteAtLast()



llist.printList()
print("\n Node Count",Node.node_count)