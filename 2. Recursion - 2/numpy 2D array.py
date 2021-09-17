
import numpy as np


    
class Solution():
    def __init__(self,arr) -> None:
        
        
        self.k = 0
        self.j = 0
    def PrintElem(self,arr):
        rows , colums = arr.shape
        if self.k == 1 and self.j ==0:
            self.k , self.k = 0 ,0
        
            return
        if self.k ==0 and self.j < colums:
                print(arr[self.k,self.j],end=' ')
                self.j +=1
        elif self.k < rows and self.j == colums :
            if self.k != 0:
                print(arr[self.k,colums-1],end=' ')    
            self.k +=1        
        
        elif self.k == rows and self.j <= colums and self.j !=0:
            if self.j != colums :
                print(arr[self.k-1,self.j-1],end=' ')
              
            self.j =self.j - 1
        else:
            if self.k != rows:
                print(arr[self.k-1,0],end = ' ')
            self.k = self.k - 1
            

        self.PrintElem(arr)
    def main(self,arr1):
        m,n = arr1.shape
        if arr1.shape ==(0,0):
            return 
        
        self.PrintElem(arr1)
        
        self.main(arr1[1:m -1 , 1:n -1])


    


