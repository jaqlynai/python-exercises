'''
Jaqlyn Ai
Feb 12 2022
Merge Sort
'''

unsorted_list = [38, 27, 43, 3, 9, 82, 10]

def merge(left, right): #left and right are sorted halves of list

    print(left, 'left')
    print(right, 'right')
    merged_list = []

    while len(left) != 0 and len(right) != 0:

        if left[0] <= right[0]:
            merged_list.append(left[0])
            left.remove(left[0])
        else:
            merged_list.append(right[0])
            right.remove(right[0])
    
    #runs if left half has more elements left
    while len(left) != 0:
        merged_list.append(left[0])
        left.remove(left[0])
    
    #runs if right half has more elements left
    while len(right) != 0:
        merged_list.append(right[0])
        right.remove(right[0])

    print(merged_list)
    return merged_list


def merge_sort(list, left, right):

    if len(list) < 2:
        print(list)
        return list
        
    else:
        
        mid = (left + right) // 2
        left_half = merge_sort(list[left:mid], 0, len(list[left:mid])) #left half
        right_half = merge_sort(list[mid:right], 0, len(list[mid:right])) #right half
        return merge(left_half, right_half)


merge_sort(unsorted_list, 0, len(unsorted_list))