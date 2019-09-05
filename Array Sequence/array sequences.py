# Python array sequences
# Array sequences in python include: List, Tuple, String.
# Algorithms involving Sequence


# Exercise 1: Write a function to check if two giving Strings are Anagrams.
# An Anagram is when the two strings can be writting using exact same letters. eg god=dog
def anagrams2(s1, s2):
    s1 = s2.replace(' ', '').lower()
    s2 = s1.replace(' ', '').lower()
        
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
   
            count[letter] = 1

    for k in count:
        if count[k] !=0:
            return False
    return True
print(anagrams2('dog', 'god'))


# Exercise 2: Given a string of words, reverse all the words eg "My best" return "best my".

def rev_word1(s):
    return " ".join(reversed(s.split()))
print(rev_word1("My best"))



# Exercise 3: Given two arrays A and B, if B was formed from reshuffled elements of A. with only one 
# element missing, find the missing element.

def find_missing(arr_a, arr_b):
    arr_a.sort()
    arr_b.sort()
    for x,y in zip(arr_a, arr_b):
        if x != y:
            return x
    return arr_a[-1]
print(find_missing([1,2,3,4,5,6,7,8,9], [2,1,4,3,6,5,7,8]))


# Exercise 4: Given a string, determine if it is comprised of all unique characters. eg 'abcd' and not aabcd

def my_check2(s):
    seen = set()
    for i in s:
        if i in seen:
            return "Not Unique"
        else:
            seen.add(i)
    return "Yes Unique"
print(my_check2("abbcde"))
            