
from cgitb import reset


def is_palindrome(i,length, array):
    
    if(array[i] != array[length-1-i]):
        return False

    mid_point = int(length/2)
    if(i >= mid_point):
        return True

    return is_palindrome(i+1,length,array)



if __name__=='__main__':
    input = "madam"
    input_arr = list(input)
    print('input array is :', len(input_arr))
    result = is_palindrome(0, len(input_arr), input_arr)
    print(result)
    print("is palindrome",result)