def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j <len(a2):
       
        
        if a1[i]<a2[j]:
            a[k]=a1[i]
            
            i=i+1
            k=k+1
        else :
            a[k]=a2[j]
            
            j=j+1
            k=k+1
        
    while i<len(a1):
        a[k]=a1[i]
        i=i+1
        k=k+1
    while j <len(a2):
        a[k] = a2[j]
        k=k+1
        j=j+1
    a 



def mergesort(a):
    if len(a)==0 or len(a)==1:
        return
    mid = len(a)//2
    a1 = a[:mid]
    a2 = a[mid:]
    
    mergesort(a1)
    mergesort(a2)
    
    merge(a1,a2,a)
   
    

l3 = [10,23,43,2,2,3,5,4]

(mergesort(l3))
