# A stack is an ordered collections of items where the addition of new items and the removal of existing 
# item always takes place at the same end known as the "top". opposite the top is known as the base
# The most resently added item in a stack is the one that is in position to be removed first.
# Stack operations 'push' and 'pop' occur at the same end i.e "Top" with the principle "LIFO" 
# LIFO "Last in First out"  


# Exercise 1: Implementation of a stack using a simple array

class Stack(object):
    def __init__ (self, limit = 10):
        self.stk = [] 
        self.limit = limit 
    def isEmpty(self):
        return len(self.stk) <= 0 
    def push(self, item):
        if len(self.stk) >= self.limit: 
            print ('Stack Overflow!' )
        else:
            self.stk.append(item)
        print ('Stack after Push',self.stk)
    def pop(self):
        if len(self.stk) <= 0:  
            print ('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()
    
    def peek(self):
        if len(self.stk) < 0: 
            print ('Stack Underflow')
            return 0
        else:
            return self.stk[-1] 
    def size(self):
        return len(self.stk) 

s = Stack(3)
print(s.isEmpty())
s.push('apple')
s.push('banana')
s.push('mango')
s.push('kewi')
print(s.peek())
print("Size is",s.size())
print(s.pop())
print(s.peek())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())

print("Exercise 2")

# Exercise 2: Implementation of a stack using a dynamic array.

class Stack(object):
    def __init__ (self, limit = 10):
        self.stk = limit*[None]
        self.limit = limit  
    def isEmpty(self):
        return len(self.stk) <= 0 
    def push(self, item):
        if len(self.stk) >= self.limit:
            print("Yes")
            self.resize()  
        self.stk.append(item)
        print ('Stack after Push',self.stk)
    def pop(self):
        if len(self.stk) <= 0:  
            print ('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()
    
    def peek(self):
        if len(self.stk) < 0: 
            print ('Stack Underflow')
            return 0
        else:
            return self.stk[-1] 
    def size(self):
        return len(self.stk)

    def resize(self):
        newStk = list(self.stk)
        print("newstark", newStk)
        self.limit= 2*self.limit
        self.stk = newStk
s = Stack(3)
print(s.isEmpty())
print(s.size())
s.push("a")
print(s.size())
s.push("b")
s.push("c")
print("len stk=lim6",s.size())
s.push("d")
print(s.size())
print(s.peek())
s.push("e")
print(s.size())

print("Stacks Problems and Solutions")
# Stacks Problems and Solutions
# Exercise 3: how stacks can be used for checking balancing of symbols.

def balance_check(s):
    if len(s) % 2 != 0:
        return "It is not balance1"
    opening = set('([{')
    matches = set([("(", ")"), ("[", "]"), ("{", "}")])
    stack = []
    not_instack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
            # print("in Stack & Opening", paren)
            # print("Stack",stack)
        else:
            not_instack.append(paren)
            # print("My paren Not in Stack", paren)
            # print("Not in Stack & Opening",not_instack)
            if len(stack) == 0: 
                return "It is not balance2"
            last_open = stack.pop()
            # print("Last_Open, My paren Not in Stack",last_open, paren )
            if (last_open, paren) not in matches:
                return "It is not balance3"
    return len(stack) == 0

print(balance_check("[({()})]"))



def isPalindrome(A):
    i = 0
    j = len(A)-1
    while (i < j and A[i] == A[j]):
        i += 1 
        j -= 1 
        print("I",i)
        print("J",j)
    if (i < j ):
        print("Not a Palindrome") 
        return False
    else: 
        print("Palindrome")
        return True 
print(isPalindrome(['s','m', 'a', 'd','a', 'm','s']))
#print(isPalindrome(["n","u","r","s","e","s","r","u","n"]))
#print(isPalindrome("nursesrun"))
#print(isPalindrome("nurses run"))



print("Palindrome Problem with Stack")

def isPalindrome2(str): 
    Stack = []
    palindrome = False
    for char in str:
        Stack.append(char) 
    for char in str:
        if char == Stack.pop():
        #if char == strStack.pop():
            palindrome = True
            # print("pop char",char) # s
            # Compare each char of str to last char in Stack
        else: 
            palindrome = False
    return  palindrome
print(isPalindrome2("smadams"))


print("Balace Braket, Narasima Solution")

class Stack2(object):
    def __init__ (self):
        self.items = []  
    def push(self, item):
        self.items.append(item)
        print ('Stack after Push:',self.items)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1] 
    def isEmpty(self):
        return self.items == []

s = Stack2()




def  check_symbol_balance(input):
    symbolstack = s
    balanced = False
    matches = set([("(", ")"), ("[", "]"), ("{", "}")])
    for symbols in input:
        if symbols in [ '(', '{', '[' ]: 
            symbolstack.push(symbols)
        else:
            if symbolstack.isEmpty():
                balanced = False
            else:
                topSymbol = symbolstack.pop()
                print("Topsymb:",topSymbol)
                print("Symb:",symbols)
            if (topSymbol, symbols) not in matches:  # this compare last elem of stack to 1st elem of d entered str if both are in matches
            #if not matches(topSymbol, symbols): # TypeError: 'set' object is not callable (ie refering to matches)
                balanced = False
            else:
                balanced = True
    return balanced
print("Check Balance:",check_symbol_balance("[({()})]"))



class Stack:
    def __init__(self):
        self.items = []

    def stk(self):
        return self.items
 
    def is_empty(self):
        return self.items == []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        #print("self.items ie the Stack",self.items)
        for item in (self.items):
            print("Item",item)
 
def insert_at_bottom(s, item1):
    if s.is_empty(): # Base case
        s.push(item1)
        print("Stack was Empty")
        print("Stack:",s.stk())
       
    else:
        
        popped = s.pop()
        print("Stack:",s.stk())    #The recursive call is for the code to run again,#
        # the condition that yield the base case can be above it such as this example popped = s.pop()
        insert_at_bottom(s, item1) # Recursive call that Result to base case &  popped = s.pop() 
        # after it achieve our base case then we push something to it
        s.push(popped)
        print("Stack-2:",s.stk())
 
def reverse_stack(s):
    if s.is_empty(): # Base Case
        pass
    else: 
        popped = s.pop() 
        reverse_stack(s) # Recursive call that Result to base case
        insert_at_bottom(s, popped) # Function Call
 
 
s = Stack()
'''s.push("a")
s.push("b")
s.push("c")'''
#print("self.items ie the Stack",self.items)
str = "abcd"
data_list = str
#data_list = input('Please enter the elements to push: ')
for data in data_list:
    s.push(data)
print('The stack:')
s.display() # Method Call
reverse_stack(s) # Function Call
print('After reversing:')
s.display()



z = ["p","o","l","i"]
def Reverse(s): 
    if len(s) ==0: 
        pass
    else: 
        popped = s.pop() 
        print("S",s)
        Reverse(s) 
        print("S",s)
print(Reverse(z))
print(z)





print("Infix to Postfix")

class Conversion:
    def __init__(self):
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
 
    def isEmpty(self):
        return (self.array == [])
  
    def peek(self):
        return self.array[-1]
  
    def pop(self):
        if not self.isEmpty():
            return self.array.pop()
        else:
            return "Stack Underflow"

    # Push the element to the stack

    def push(self, op):
        self.array.append(op)
 
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than precedence of opera on top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            print("a",a)
            print("b",b)
            print("Self.precedence",self.precedence)
            print("i:",i)
            print("self.peak",self.peek())
            print("Our Stack",self.array)
            
            return True if a <= b else False
        except KeyError:
            return False
    # The main function that# converts given infix expression# to postfix expression
    def infixToPostfix(self, exp):
        for i in exp:
           
            # If the character is an operand,
            # add it to output
            if self.isOperand(i): #True for any i that is alphbet
                self.output.append(i)
                print("Operands or chars",self.output)
                print("I1:",i)
            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)
          
            elif i == ')':
               
                while((not self.isEmpty()) and  # if something is in the stack and top of stack isnot (
                      self.peek() != '('):

                    a = self.pop()

                    self.output.append(a)

                if (not self.isEmpty() and self.peek() != '('):

                    return -1

                else:

                    self.pop()

            else:

                while(not self.isEmpty() and self.notGreater(i)):

                    if i == "^" and self.array[-1] == i:

                        break

                    self.output.append(self.pop())

                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        print( "".join(self.output))
 
# Driver program to test above function

exp = "a+b*(c^d-e)^(f+g*h)-i"
exp2 = "3*(4+2)*5"
#obj = Conversion(len(exp)) # capacity
obj = Conversion()

obj.infixToPostfix(exp)
#print("notGreater",obj.notGreater(exp))
print("is it operand?:",obj.isOperand('+'))

