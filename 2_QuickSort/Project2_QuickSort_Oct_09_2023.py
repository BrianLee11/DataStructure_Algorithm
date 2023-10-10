"""
QuickSort algorithm
1) the pivot number is important
2) uses recursive method
3) uses divide-and-conquer (partition) method
"""

# given array
# we want to sort this array without creating a new array
# target = [1,1,1,2,3,3,5,6,8]
array  = [3, 1, 1, 6, 3, 8, 2, 1, 5]

""" part 1: sort array so that 
1) elements less than or equal to the pivot (defined as the last element) is 
on the left of the pivot
2) elements more than or equal to the pivot is on the right 
"""
    
# define the pivot as the last elemt of the given array
pivot = array[len(array)-1]

# the 'left pointer' is described as i 
# the 'right pointer' is described as j 
i = 0
j = len(array) - 2

while(True):    
    # the left pointer is moved until an element bigger than pivot is reached
    while (array[i] < pivot and i < j):
        i = i + 1

    # the right pointer is moved until an emelemnt smaller than pivot is reached
    while (array[j] > pivot and i < j):
        j = j - 1

    # swap the misplaced numbers   
    if i<j:
        array[i], array[j] = array[j], array[i]
    
    # break condition: i>j 
    else: 
        array[i], array[len(array)-1] = array[len(array)-1], array[i]
        break

#print(array) # output: [3, 1, 1, 1, 3, 2, 5, 6, 8]
# now let's move to part 2: we want the final result to be:
# target = [1,1,1,2,3,3,5,6,8]

# part 2
array2  = [3, 1, 1, 6, 3, 8, 2, 1, 5]

def partition (array, low, high):
    pivot = array[high - 1] # last element
    i = low
    j = high - 2
    
    while (i <= j):
        
        while (array[i] <= pivot and i <=j):
            i = i + 1
            
        while (array[j] >= pivot and i <= j):
            j = j - 1
        

        if i < j:
            # swap
            array[i], array[j] = array[j], array[i]
    
    # swap the pivot and the array[i]
    array[i], array[high -1] = array[high - 1], array[i]

    # return pivot index
    return i 

def quickSort (array, low, high):
    if high - low > 1: # has two or more elements in an array
        pivot_index = partition(array, low, high)
        quickSort(array, low, pivot_index)
        quickSort(array, pivot_index + 1, high)

quickSort(array2, 0, len(array2))
print(array2) #output: [1, 1, 1, 2, 3, 3, 5, 6, 8]