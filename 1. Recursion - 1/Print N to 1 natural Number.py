'''
Question -
Print natural numbers from n to 1 using recursion

sample input -
5
sample output
5
4
3
2
1

'''

def Sequence(n):
    if n ==0:
        return
    print(n)
    Sequence(n-1)
    

if __name__=='__main__':
    number = int(input('enter the number '))
    Sequence(number)