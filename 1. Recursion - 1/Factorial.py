'''
Question -
create a function to calculate the factorial of a given number using recursion.

Sample Input -
5

Sample Output -
120

'''

def factorial(n):
    if n==0 or n ==1:
        return 1
    Multiplication = n * factorial(n-1)
    return Multiplication

if __name__=='__main__':
    number = int(input('enter the number '))
    factorial_of_number = factorial(number)
    print(factorial_of_number)
