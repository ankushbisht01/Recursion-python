"""
    Question -
    Create a function that take a number and return the term correspomding to the number from fibonacci series

    Sample Input -
    5

    Sample Output -
    5

"""

def febon(n):
    if n == 1 or n==2:
        return True
    fabi_n_1 = febon(n-1)
    fabi_n_2 = febon(n-2)
    sum = fabi_n_1 + fabi_n_2
    return sum

if __name__=='__main__':
    number = int(input('enter the number '))
    term = febon(number)
    print(term)
