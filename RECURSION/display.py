

from audioop import reverse
from unicodedata import name

arr = [1,2,3,4,5,10,0]

# Object references are passed by value.
def swap(l,r,array):
    array[l], array[r] = array[r], array[l]
    return


# swapping an array using two pointers
def reverse_array(left, right, array):
    
    if(left >= right):
        print("After swapping: ", array)
        return
    swap(left, right, array)

    left = left + 1
    right = right - 1

    reverse_array(left, right,array)

# swapping an array using only one pointers
def reverse_array_one_pointer(index,length,array):

    middle = int(length/2)

    if(index >= middle):
        print("After swapping: ", array)
        return

    right = (length - 1 - index)

    swap(index, right, array)

    left = index + 1

    reverse_array_one_pointer(left, length,array)



if __name__=='__main__':
    print("Before swapping an array :", arr)
    reverse_array_one_pointer(0,len(arr), arr)