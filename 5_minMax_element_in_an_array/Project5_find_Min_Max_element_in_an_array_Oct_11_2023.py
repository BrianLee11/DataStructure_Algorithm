"""
Task: given an array with numbers, find the minimum and maximum numbers of this array
"""
"""
pseudo codes 

input: array with n-number of numbers
output: minimum number in the array, maximum number in the array

def minMax(array):

	// initialize variables
	max = array[0]
	min = array[0]

	for each i from 1 to len(array) do:
		
		// case 1: array[i] >= previous max
		if array[i] >= max then:
			
			# update the max
			max <- array[i]
		
		// case 2: array[i] < previous min
		//condition to update the min?
		else if array[i] < min then:
				// update the min
				min <- array[i]
		end if
	end for

	return max, min
end function

Time complexity: O(n^2)  (each i visiting case 1 and case 2 every time)
"""


# Python codes
def minMax(array):
    
    max = array[0]
    min = array[0]
    
    for i in range(1, len(array)-1):
        if array[i] >= max:
            max = array[i]
            
        elif array[i] < min:
            min = array[i]
        
    return max, min

# test
array = [1,3,5,4,3, -1, 6, -20, 3, 50, 1,2,3,4]
print(minMax(array)) #output: (50, -20)