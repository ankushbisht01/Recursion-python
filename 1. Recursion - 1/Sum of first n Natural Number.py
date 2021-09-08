'''
Question -
Create a program to return sum of first n natural number using recursion

sample input -
3

sample output (sum of first 3 natural number)-
6
'''

def Sum(n):
    if n==1:
        return n
    Sum_of_n = n+Sum(n-1)
    return Sum_of_n

