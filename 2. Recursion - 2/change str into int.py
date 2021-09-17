'''
Question - 
Change string type integers to integer type integer using recursion
Sample Input - 
'1234'
Sample Output - 
1234
Condition  -
No use of pre definied python function
'''

def ChangeType(n):
    
    RefernceDic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    if len(n)==0:
        return 0
    smaller_num = ChangeType(n[:-1])
    
    return smaller_num*10+RefernceDic[n[len(n)-1]]

def main():
    input_str = input('enter the number string: ')
    integer_number = ChangeType(input_str)
    print(integer_number)
    print('type of new object: ', type(integer_number))

if __name__ =='__main__':
    main()