'''
Function:
    implement insert sort algorithom. 
    1. insert a integer in a sorted array
    2. sort an unsorted array

Author:
    Jack

Date:
    Dec 2018

'''

def insert_sort(unsorted_array):
    '''
    Implement insert sort algorithm, to sort an unsorted array, and return 
    a sorted array

    Arguments:
    unsorted_array  -- input unsorted array, integers

    Returns:
    sorted_array    -- sorted array of integers
    '''

    sorted_array = []
    for x in unsorted_array:
        # sorted_array is Null
        if len(sorted_array) == 0:
            sorted_array.append(x)
        else:
            for i in range(0, len(sorted_array)):
                # insert x before i if x < sorted_array[i]
                if x < sorted_array[i]:
                    sorted_array.insert(i, x)
                    break

            # x is greater than all elements of sorted_array
            if not (x in sorted_array):
                sorted_array.append(x)

    return sorted_array


if __name__ == '__main__':

    str = input('input a serial integer numbers:')
    str_split = str.split(' ')
    
    unsorted_array = []
    for x in str_split:
        if x != '':
            unsorted_array.append(int(x))
    print( 'orginal array:', unsorted_array )
    
    sorted_array = insert_sort(unsorted_array)
    print('sorted array:', sorted_array)
