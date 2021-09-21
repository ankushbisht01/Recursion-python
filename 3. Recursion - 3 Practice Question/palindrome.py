'''
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false

'''

def Palindrome(str1:str):
    if len(str1)==1:
        return str1
    reversed_str = Palindrome(str1[1:])
    return reversed_str +str1[0]

def main():
    input_str = input('enter the number you want to check : ')
    reversed_str = Palindrome(input_str)
    
    if input_str == reversed_str:
        print(True)
    else:
        print(False)

if __name__=='__main__':
    main()