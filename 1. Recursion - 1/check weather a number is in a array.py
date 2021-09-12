'''
Question - 
Create a function that will search for an element in an array using recursion
Sample input -
[1,3,4,5,5,6,7,8,9],4
sample output
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
    
def Search2(N,L,x):
    try:
        if N[0]==x:
            return L- len(N)
        last_search = Search2(N[1:],L,x)
        return last_search
    except:
        return 'the element you are searching isnt present in the array'

