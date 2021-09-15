'''
Problem Statement: Remove X
Problem Level: MEDIUM
Problem Description:
Given a string, compute recursively a new string where all 'x' chars have been removed.
Input format :
'''

def RemoveX(str1):
    if len(str1)==0:
        return str1
    new_str = RemoveX(str1[1:])
    

    if str1[0].lower() =='x':
        return ''+new_str
    else:
        return str1[0]+new_str

def RemoveX1(str1):
    if len(str1)==0:
        return str1
    first_element = str1[0]
    str1 = RemoveX1(str1[1:])
    
    if first_element.lower() =='x':
        return ''+str1
    else:
        return first_element+str1

def main():
    input_string = input('enter the string: ')
    replaced_string = RemoveX1(input_string)
    print(replaced_string)

if __name__ == '__main__':
    main()