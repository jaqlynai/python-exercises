'''
Jaqlyn A
Feb 12 2022
Recursive Binary Search
'''

#list of randomly generated integers to check from
search_list = [21, 25, 32, 36, 42, 47, 52, 61, 77, 79, 86, 88, 100, 102, 107, 108, 112, 127, 153, 163, 185, 200, 201, 206, 207, 207, 208, 209, 
215, 228, 237, 246, 262, 266, 300, 312, 313, 313, 318, 323, 325, 348, 350, 353, 359, 382, 386, 389, 396, 398, 403, 409, 410, 415, 418, 428, 482, 484, 
489, 503, 525, 549, 569, 607, 642, 647, 650, 657, 664, 673, 688, 693, 712, 713, 715, 718, 725, 727, 730, 748, 748, 755, 757, 757, 758, 768, 780, 789, 
809, 832, 840, 867, 873, 882, 891, 916, 922, 930, 949, 990]

def binary_recursive(num):
    mid = len(search_list) // 2

    if num == search_list[mid]:
        return True

    elif mid <= 0:
        return False

    else:
        if num > search_list[mid]:
            del search_list[:mid]
            return binary_recursive(num)

        else:
            del search_list[mid:]
            return binary_recursive(num)

while True:
    user_num = input('Enter integer here: ')

    try:
        user_num = int(user_num)
        break

    except ValueError:
        print('Please enter an integer value.')

if binary_recursive(user_num):
    print('Found')
else:
    print('Not found')