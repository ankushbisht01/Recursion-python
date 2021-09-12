'''
Question - 
create a function that will return wheater a array is sorted or not 
Sample Input -
[1,2,3,4,5,6]
Sample Output - 
True 
'''


def BetterSorting(l,el):
    if l[0]==el or l[len(l)-1] ==el :
        return True
    if l[li]>l[li +1]:
        return False