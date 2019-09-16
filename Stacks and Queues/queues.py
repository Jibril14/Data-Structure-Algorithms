# A queue is an ordered collection of items where the addition of new items begins at one end called the rear
# and the removal of existing items occur at the opposite end call the front
# queue is similar to stack except that the item that has been in the collection the longest is at the front and in
# the position to be remove first.
# queue is perform base on FIFO principle
# Dequeue is the term use to describe the Removal/Deletion of the first item in a queue
# Enqueue is the term use to describe the addition of new items to the rear of the queue


# Exercise 1: Implementation of a queue using a simple array

class  Queue:
    """ A class that implement a fixed size Queue """
    def __init__(self, limit = 10):
        self.items = []
        self.limit = limit

    def __len__(self):
        """ Supports the len protocol """
        return len(self.items)

    def is_empty(self):
        return self.__len__() == 0 
    
    def enqueue(self, item):
        if self.__len__() >= self.limit:
            print("Stack Overflow!")
            return 
        else:
            self.items.append(item)

    def dequeue(self):
        if self.__len__() <= 0:
            print("Stack Underflow!")
            return
        else:
            self.items.pop(0)
    
    def peek(self):
        return self.items[0]

    def __str__(self):
        return 'Queue: ' + str(self.items)

q = Queue(5)
print(q.is_empty())
print(len(q))
q.enqueue("item1")
q.enqueue("item2")
q.enqueue("item3")
q.enqueue("item4")
q.enqueue("item5")
q.enqueue("item6") # Never got Appended
print("Len:",len(q))
print(q.peek())
q.dequeue()
q.enqueue("item7")
q.enqueue("item8")
print(q.peek())
print(q)

print('Class attributes')
print(Queue.__doc__) # One of Intrincic attribute authomatically giving us by our class




# Implementing a queue using a simple array may not just be enough since after dequeing some front items
# of the queue, addition of new items does not occupy the free empty slot at the begginning. solution is to use a 
# Circular array.

# Exercise 2: How to implement a queue using a circular array.

class CircularQueue:
    """Circular queue with a fixed capacity"""

    def __init__(self, limit = 5):
        self.limit = limit
        self.array = [None] * self.limit
        self.front = 0  
        self.rear = 0
        self.size = 0
        

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peak(self):
        return self.array[self.front]

    def enqueue(self, data):
        if self.size >= self.limit:
            raise Exception("QUEUE IS FULL")

        self.array[self.rear] = data

        # The rear and size get incremented by one after every enqueue
        print("front:", self.front)
        print("rear:", self.rear)
        self.rear = (self.rear + 1) % self.limit
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            raise Exception("UNDERFLOW")

        # The front get incremented by one after every dequeue while size decrease by one
        print("front1:", self.front)
        temp = self.array[self.front]
        self.array[self.front] = None

        # Grab the front index and set it to None
        print("array:",self.array)
        self.front = (self.front + 1) % self.limit
        self.size -= 1
        return temp
        


q = CircularQueue(5)
print("Len",len(q))
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.dequeue()
q.enqueue("F")
print(q.peak())
print("Array:", q.array)




# Exercise 3: How to implement a queue using two Stacks.

class Q:
    def __init__(self):
        self.S2 = []
        self.S1 = []
    
    def enqueue(self, item):
        self.S1.append(item) 
    
    def dequeue(self):
        if not self.S2:
            while self.S1:
                self.S2.append(self.S1.pop())
        return self.S2.pop()

q1 = Q()
for i in range(5):
    q1.enqueue(i)
for i in range(5):
    print (q1.dequeue())


# Exercise 4: How to implement a double ended queue.

      
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def myArray(self):
        return self.items

d = Deque()
d.addFront('A')
d.addFront('B')
d.addFront('C')
d.addRear('D')
d.addRear('E')
d.addRear('F')
d.removeFront()
d.removeRear()
print(d.myArray())



# Exercise 4: Given a queue of integers, rearrange the elements by interleaving the first half of the
# list with the second half of the list eg giving [11, 12, 13, 14, IS, 16, 17, 18, 19, 20.] return
#  [11, 16, 12, 17, 13, 18, 14, 19, 15, 20] 

class QQueue:
    def __init__(self):
        self.array = []
    
    def isEmpty(self):
        return len(self.array) == 0

    def enQueue(self, item):
        return self.array.append(item)

    def deQueue(self):
        return self.array.pop(0)

    def myArray(self):
        return self.array

    def size(self):
        return len(self.array)

class SStack:
    def __init__(self):
        self.array =  []
    
    def isEmpty(self):
        return len(self.array) == 0
    
    def push(self, item):
        return self.array.append(item)

    def pop(self):
        return self.array.pop()
    
    def myArray(self):
        return self.array


def interLeavingQueue(que):
    stk = SStack() 
    halfSize = que.size() //2 

    for i in range(0, halfSize):
        stk.push(que.deQueue())
    
    while not stk.isEmpty():
        que.enQueue(stk.pop())

    for i in range(0, halfSize):
        que.enQueue(que.deQueue())

    for i in range(0, halfSize):
        stk.push(que.deQueue())

    while not stk.isEmpty():
        que.enQueue(stk.pop())
        que.enQueue(que.deQueue()) 

que = QQueue()
que.enQueue(1)
que.enQueue(2)
que.enQueue(3)
que.enQueue(4)
que.enQueue('A')
que.enQueue('B')
que.enQueue('C')
que.enQueue('D')

interLeavingQueue(que) 
while not que.isEmpty():
    print(que.deQueue())
   


# Exercise 5: Given an integer k and a queue of integers, how do you reverse the order of the first k
# elements of the queue, leaving the other elements in the same relative order? For example, if k=4 
# and queue has the elements [ 10, 20, 30, 40, 50, 60, 70, 80, 90); the output should be
# [40, 30, 20, 10, 50, 60, 70, 80, 90].

def reverseQueueFirstKElements(que, k):
    stk = SStack()
    if que == None or k > que.size():
        return
    for i in range(0, k):
        stk.push(que.deQueue())
    while not stk.isEmpty():
        que.enQueue(stk.pop())
            
    for i in range(0, que.size() - k):
        que.enQueue(que.deQueue()) 

que = QQueue()
que.enQueue(11)
que.enQueue(12)
que.enQueue(14)
que.enQueue(15)
que.enQueue(16)
que.enQueue(17)
que.enQueue(18)

reverseQueueFirstKElements(que, 4) 
while not que.isEmpty():
    print(que.deQueue())



# Exercise 4: Given a string, check whether it is a palindrome or not using a doubly ended queue.

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
            self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items) 

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
print(palchecker("lsdkjfskr"))
print(palchecker("madam"))
