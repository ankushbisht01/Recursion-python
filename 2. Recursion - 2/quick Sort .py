'''
QUICK SORT ALGORITHM 

'''
def OrderElem(n,si,li):
    first_elem = n[si]
    count = 0
    starting_index = si
    
    while starting_index <= li:
        
        if n[starting_index] < first_elem:
            count+=1
        starting_index +=1
    
    n[si] , n[si+count] = n[si+count] , n[si]
    count = si + count
    
    starting_index = si
    ending_side = li
    while starting_index < count and ending_side >count:
        if n[starting_index]>n[count]:
            if n[ending_side]<n[count]:
                n[starting_index] , n[ending_side] = n[ending_side],n[starting_index]
                starting_index+=1
                ending_side-=1
                
            else:
                ending_side-=1
                
        elif n[ending_side]<n[count]:
            if n[starting_index]>n[count]:
                n[starting_index] , n[ending_side] = n[ending_side],n[starting_index]
                starting_index+=1
                ending_side-=1
            else:
                starting_index-=1
        else:
            starting_index+=1
            ending_side-=1
    
    return count


def QuickSort(n,si,li):
    
    if si >= li:
        return None
    i = OrderElem(n,si,li)
    
    
    QuickSort(n,si,i-1)
    QuickSort(n,i+1,li)
    

arr = [2,34,21,56,223, 23, 58, 56]

QuickSort(arr,0,len(arr)-1)
print(arr)
