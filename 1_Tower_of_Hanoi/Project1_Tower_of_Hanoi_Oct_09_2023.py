"""
Description of the Tower of Hanoi algorithm

Three simple rules are followed:
0. There are 3 rods. 
    
1. Only one disk can be moved at a time.

2. Each move consists of taking the upper disk from one of the stacks and 
placing it on top of another stack. 
In other words, a disk can only be moved if it is the uppermost disk on a stack.

3. No larger disk may be placed on top of a smaller disk.

The number of the least movements = 2^n - 1 
where n = number of discs
"""

# the number of movements of discs
count = 0

def PRINT(origin, destination):
    print("Move the top disk from rod", origin, "to rod", destination)

def MOVE(n, start, end):
    
    # declare the variable count as global so that used outside function
    global count
    
    # when the only 1 disc exists in a rod
    if n == 1:
        PRINT(start, end)
        count = count + 1
        
    # recurisve cases
    else:
        # a nice trick to alternate to locate the other rod
        other = 6 - start - end
        
        # need to move all n-1 discs to the 'other' rod so that only 1 disc
        # remains in the 'start' rod
        MOVE(n-1, start, other)
        
        # when only 1 disc remains in a rod
        # the 1 disc moves from the starting rod to ending rod
        PRINT(start, end)
        count = count + 1
        
        # now need to move all n-1 rods from the 'other' rod to the 'end' rod
        MOVE(n-1, other, end)


# example
MOVE(4, 1, 3)
print(count) # output: 15 = 2^4 - 1 = 16 - 1

# another example
count = 0
MOVE(5,1,3)
print(count) # output: 31 = 2^5 - 1 = 32 - 1