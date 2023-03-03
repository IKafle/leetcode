


def print_name_n_times(n):
    print("ishwor kafle")

    if (n == 1):
        return
    print_name_n_times(n-1)


def print_linearly_from_1_to_n_up(index,n):

    print(index)

    if(index == n):
        return
    print_linearly_from_1_to_n_up(index+1, n)


def print_linearly_from_1_to_n_down(n):

    if(n == 0):
        return

    print_linearly_from_1_to_n_down(n-1)
    print(n)


    
if __name__=="__main__":
    print_linearly_from_1_to_n_down(10)
