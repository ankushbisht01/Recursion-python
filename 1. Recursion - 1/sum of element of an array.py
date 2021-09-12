'''
Question - 
create a function that calculate the sum of all element of an array using recursion

Sample input - 
[2,3,5,3]

Sample Output - 
10

'''


def Sumarray(L):

    if len(L)==1:
        return L[0]
    elif len(L)==0:
        return
    
    last_element_sum = Sumarray(L[:len(L)-1])
    sum = L[-2] + last_element_sum
    return sum


if __name__=="__main__":
    input_array = eval(input('enter the array with sqare breaces: '))
    array_sum = Sumarray(input_array)
    print('Sum of the given array is :',array_sum)