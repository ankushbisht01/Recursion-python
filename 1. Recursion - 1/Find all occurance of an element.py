'''
Problem Statement: All indexes of x
Problem Level: MEDIUM
Problem Description:
Given an array of length N and an integer x, you need to find all the indexes where x is present in the input array. Save all the indexes in an array (in increasing order).
Do this recursively. Indexing in the array starts from 0.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format :
indexes where x is present in the array (separated by space)
'''
    
        
    
    
    
def AllSearch(N,L,x):
    if len(N)==0:
        print('\n')
        return 
    if N[0]== x:
        print( L- len(N) , end = ' ')
    last_search =  AllSearch(N[1:],L,x) 
    
     
def main():
    length = int(input('enter the length of array : '))
    array_element = input('enter the element of the array seperted by space : ')
    elem = eval(input('enter the element you want to search in the array: '))
    array = array_element.split(' ')
    arr = [eval(x) for x in array]
    AllSearch(arr , length , elem)


if __name__ == '__main__':
    main()
