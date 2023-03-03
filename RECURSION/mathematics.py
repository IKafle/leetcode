

def display_sum_n_natural_numbers(num):

    if (num == 0):
        return 0

    return num + display_sum_n_natural_numbers(num-1)


def display_factorial(num):

    if num ==0:
        return 1

    return num * display_factorial(num-1)


def display_nth_fibo(num):
    if (num <= 1):
        return num

    first = display_nth_fibo(num-1)
    second =display_nth_fibo(num-2)

    return first + second


if __name__=='__main__':
    num = 5
    print(f"Sum of {num} natural numbers", display_sum_n_natural_numbers(num))
    print(f"Factorial of {num} natural numbers", display_factorial(num))
    print(f"{num} th fibo number", display_nth_fibo(num-1))
