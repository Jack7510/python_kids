'''
Function:
    implement binary insert sort algorithom. 
    1. insert a integer in a sorted array
    2. sort an unsorted array

Author:
    Jack

Date:
    Dec 2018

'''

def binary_insert_sort(unsorted_array):
    '''
    Implement binary insert sort algorithm, to sort an unsorted array, and return 
    a sorted array

    Arguments:
    unsorted_array  -- input unsorted array, integers

    Returns:
    sorted_array    -- sorted array of integers
    '''

    sorted_array = []
    for x in unsorted_array:
        sorted_array_len = len(sorted_array)
        # sorted_array is Null
        if sorted_array_len == 0:
            sorted_array.append(x)
        elif x <= sorted_array[0]:
            sorted_array.insert(0, x)
        elif x >= sorted_array[-1]:
            sorted_array.append(x)
        else:
            start, end = 0, sorted_array_len - 1
            while True:
                mid = start + (end - start) // 2
                #print(start, mid, end)
                if mid == start:
                    if x < sorted_array[mid]:
                        sorted_array.insert(mid, x)
                    else:
                        sorted_array.insert(mid+1, x)
                    break
                else:
                    if x < sorted_array[mid]:
                        end = mid
                    else:
                        start = mid
        print('sorting: ', sorted_array)
                        
    return sorted_array


if __name__ == '__main__':

    str = input('input a serial integer numbers:')
    str_split = str.split(' ')
    
    unsorted_array = []
    for x in str_split:
        if x != '':
            unsorted_array.append(int(x))
    print( 'orginal array:', unsorted_array )
    
    sorted_array = binary_insert_sort(unsorted_array)
    print('sorted array:', sorted_array)
