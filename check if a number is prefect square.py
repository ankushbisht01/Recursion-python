
'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
'''


def Solution():
    def __init__(self,number):
        self.length = len(str(number))
        self.number = number
    def sum1(self):
        if self.number ==0 :
            return 0
        remainder = self.n %10
        quotient = self.n //10
        return remainder + self.Sum1(quotient)

    def CheckSsquare(self):
        unit_digit = self.number // 10 **(self.length-1)
# 1, 4 , 9, 16
#2,3,5,6,7,8,10