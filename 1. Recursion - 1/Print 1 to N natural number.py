'''
Question -
Print natural numbers from 1 to n using recursion

sample input -
5
sample output
1
2
3
4
5
'''

def Sequence(n):
    if n ==0:
        return
    Sequence(n-1)
    print(n)

if __name__=='__main__':
    number = int(input('enter the number \n'))
    Sequence(number)