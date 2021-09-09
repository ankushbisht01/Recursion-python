'''
Question - 
create a function to check wheather a list is sorted or not

sample Input - 
[1,3,4,5,6,4]

SAmple Output-
False
'''

def Sorting(L):
    if len(L)==0 or len(L)==1:
        return True
    if L[0]>L[1]:
        return False
    smallerList = L[1:]
    issmallerlistsorted = Sorting(smallerList)
    
    if issmallerlistsorted:
        return True
    else :
        return False

if __name__=="__main__":
    input_list = eval(input('enter the list'))
    result = Sorting(input_list)
    print('input list is :',result)