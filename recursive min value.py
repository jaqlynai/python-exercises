'''
Jaqlyn Ai
Feb 14 2022
Recursive Minimum Value
'''

sort_list = []

def recursive_min(numlist):

    for value in numlist:
        if type(value) != list:
            sort_list.append(value)

        else:
            recursive_min(value) #recursive call to retrieve values of sublists
    
    sort_list.sort()
    return(sort_list[0]) #returns minimum numerical value

print(recursive_min([2, 9, [1, 13], 8, 6])) #should be 1
print(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])) #should be 1
print(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])) #should be -7
print(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])) #should be -13