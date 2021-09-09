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
    element_n_1 = Sorting(L[:len(L)-2])
    
    if L[len(L)-2]<=L[len(L)-1]:
        return True
    else:
        return False

if __name__=="__main__":
    input_list = eval(input('enter the list'))
    result = Sorting(input_list)
    print('input list is :',result)