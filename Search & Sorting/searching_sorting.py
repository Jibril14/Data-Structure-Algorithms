# Sorting algorithm include: Selection sort, bubble sort, merge sort etc
# Sorting elements of an array before searching, makes searching much faster
# Some searching algorithm are Linear search, Binary search etc

def binary_search(list, item):
    low = 0 
    high = len(list) - 1
    while low <= high: 
        mid = (low + high)
        guess = list[mid]
    if guess == item:
        return mid
    if guess > item: 
        high = mid - 1
    else: 
        low = mid + 1
    return None 
my_list = [1, 4, 9, 13, 25, 40, 60] 
print(binary_search(my_list, 25)) 
print(binary_search(my_list, -1) )



print("\nMerge Sort")

def merge_sort(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
arr = [12,1,5,4,8,6,10,1,30]
merge_sort(arr)
print(arr)