'''
Question - 
Create a function that will search for an element in an array using recursion else return -1
Sample input -
[1,3,4,5,5,6,7,8,9],5
sample output
-1
'''


    
def Search2(N,L,x):
    try:
        if N[0]==x:
            return L- len(N)
        last_search = Search2(N[1:],L,x)
        return last_search
    except:
        return -1

