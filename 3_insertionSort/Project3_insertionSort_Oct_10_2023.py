"""
Topic: Insertion Sort Algorithm

Keyword: "sort playing cards in your hands"

Idea: Insertion sort is a simple sorting algorithm that works similar to the 
way you sort playing cards in your hands. 

The array is virtually split into a sorted and an unsorted part. 

Values from the unsorted part are picked and placed at the correct position 
in the sorted part.
(source: geeks for geeks)
"""

array = [3, 4, 1, 3, 6, 4, 1]
# we want to sort this array in ascending order: [1,1,3,3,4,4,6] 

def insertionSort(array):
    for i in range(1, len(array)): # element array[0] does not need to be sorted
        j = i
        
        # construct conditions to sort "like playing cards"
        while (j > 0 and array[j-1] > array[j]):
            
            # swap
            array[j-1], array[j] = array[j], array[j-1]
            
            # move the index j to the left 
            j = j -1 

# example
insertionSort(array)
print(array) # output: [1, 1, 3, 3, 4, 4, 6]
        