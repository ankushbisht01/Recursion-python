'''

Given a string S, remove consecutive duplicates from it recursively.
Input Format :
String S
Output Format :
Output string
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string
Sample Input 1 :
aabccba
Sample Output 1 :
abcba
Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz
'''

def RemoveConsDuplicate(x):
    if len(x)==1:
        return x
    smaller_string = RemoveConsDuplicate(x[1:])
    
    if x[0]==x[1]:
        return x[0]+smaller_string[1:]
    else:
        return x[:2]+smaller_string[1:]

def main():
    input_string = input('enter the string which you want to convert:  ')
    string_with_replaced_pi = RemoveConsDuplicate(input_string)
    print(string_with_replaced_pi)

if __name__ == '__main__':
    main()