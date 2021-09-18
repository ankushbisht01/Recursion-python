'''
Question - 
create a fucntion to return the sum of all the digits of a given int using recursion

'''

import time 


def Sum1(n):
    if n ==0 :
        return 0
    remainder = n %10
    quotient = n //10
    return remainder +Sum1(quotient)



