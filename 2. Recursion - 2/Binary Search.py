'''
Binary Search Alogirithm 

'''


def BinarySearch(L,SiartingIndex, endingIndex,elem):
    if SiartingIndex > endingIndex:
        return -1

    mid = (SiartingIndex+endingIndex)//2
    if L[mid]==elem:
        return mid
    elif mid > elem:
        return BinarySearch(L,SiartingIndex,mid-1,elem)
        
    else:
        return BinarySearch(L,mid+1,endingIndex ,elem)
        
    
def main():
    array = eval(input('enter the sorted array for Binary Search: '))
    length = len(array)
    elem = int(input('enter the element : '))
    elem_index = BinarySearch(array,0,length,elem)
    print(elem_index)

if __name__ == '__main__':
    main()