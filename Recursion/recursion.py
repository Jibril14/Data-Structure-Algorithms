# A function is a block of code which only runs when it is called
# We can pass data known as parameters into a function
# a function can return a data as a result.


# Exercise 1: Write a function to check if a single number is an even
def num_sum(n):
    if len(str(n)) == 1:
        print(n)
        return n
        
    else:
        return n%10 + num_sum(n//10)

result = num_sum(92345)
print(result)
print(type(result))
print(12345%10)
print(12345//10)
print(5+1234)
print(1239+15)


# Exercise 2: Write a recursive function to compute the factoria of a number. n! = n*(n-1), if n = 0, n!=1
#3*(2)(1)
def compute_fac(n):
    if n==0:
        return 1
    else:
        return n * compute_fac(n-1)
print(compute_fac(4))

# Exercise 3: Write a function to to compute the sum of n integer Eg if n=3, return 1+2+3 or 3+2+1(ie n + sumFirstN(n-1))
def sumFirstN(n):
    if n==0:
        return 2
    else:
        return sumFirstN(n-1) + n

def main():

    x = int(input("Please enter a non-negative integer: "))
    s = sumFirstN(x)
    print("The sum of the first", x, "integers is", str(s)+".")
if __name__ == "__main__":
    main()
print(sumFirstN(5))


# Exercise 4: Write a recursive function to implement a fibonnaci sequence
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print( fib(10))


# Exercise 5: Write a function to to compute the sum of n integer Eg if n=3, return 1+2+3
print(12345%10)
print(12345//10)
print(1234//10)
print(123//10)
print(12//10)
print(5+1234+123+12+1)

# Exercise 6: Write a function that return the reverse of a list
def revList(lst): 
    accumulator = []
    for x in lst:
        accumulator = [x] + accumulator
       # accumulator.append(x)
        print("accumulat", accumulator)
    return accumulator
def main():
    print(revList([1,2,3,4]))
if __name__ == "__main__":
    main()
print(revList(['fadw', 'boy', 'ran','mad']))

# Exercise 7: Write a function that return the reverse of a list
def revList(lst):    # Here is the 
    if lst == []:
        return []
    restrev = revList(lst[1:]) 
    first = lst[0:1]

    result = restrev + first
    return result
print(revList([1,2,3,4]))
print(revList(['fadw', 'ream', 'kodo','abdul']))

def revString(s):
    if s == "":
        return ""


    if len(A) == 1:
        return True
    return A[0] <= A[1] and isSorted(A[1:])
B= [1127, 220, 246, 277, 321, 454, 534, 565, 9331]
print(isArraylnSortedOrder(B)) 
