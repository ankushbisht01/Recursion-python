def Hanoi(n,s,a,d):
    if n ==1 :
        print('we will have to move 1 disk ' ,s ,  d )
        return 
   
    Hanoi(n-1,s,d,a)
    print('we will have to move ',n,'disk',s,d)
    Hanoi(n-1,a,s,d)


Hanoi(4,'a','b','c')