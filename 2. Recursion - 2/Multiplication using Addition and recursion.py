'''
Problem Statement: Multiplication (Recursive)
Problem Level: EASY
Problem Description:
Given two integers M & N, calculate and return their multiplication using recursion.
You can only use subtraction and addition for your calculation. No other operators are allowed.
Input format :
Line 1 : Integer M
Line 2 : Integer N
'''

def Multiplication(M , N):
    if N == 0 :
        return 0
    multipy_number = Multiplication(M,N-1)
    return M + multipy_number

def main():
    first_number = int(input('enter the first number: '))
    second_number = int(input('enter the second number: '))
    Multiplication_first_second = Multiplication(first_number,second_number)
    print(Multiplication_first_second)

if __name__ =='__main__':
    main()

