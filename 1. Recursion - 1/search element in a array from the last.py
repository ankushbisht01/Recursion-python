'''
Question - 
create a function to search a given element in an array from the end of the array using recursion if not found return -1

Sample input - 
[1,2,2,3,4,5]
Sample Output - 
2
'''




def Search(l,x):
    if l[-1]==x:
        return len(l)-1
    try:
        last_element = Search(l[:len(l)-1],x)
        return last_element
    except IndexError:
        return 'Didnt present in the array'

