'''
Question - 
create a function that will return wheater a array is sorted or not 
Sample Input -
[1,2,3,4,5,6]
Sample Output - 
True 
'''


def BetterSorting(l,el):
    length = len(l)
    
    if el == length -1 or length == 1 :
        return True
    if l[el] > l[el +1]:
        return False
    check_for_sorting = BetterSorting(l,el+1)
    if check_for_sorting == True:
        return True
    else: 
        return False

if __name__=='__main__':
        input_array = eval(input('enter the array with square brackes : '))
        Start_index = int(input('enter the index from where you want to start checking for sorting:  '))
        print(BetterSorting(input_array,Start_index))