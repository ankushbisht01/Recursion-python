'''
Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
using recursion.
Input format :
Integer k
Output format :
Geometric sum (upto 5 decimal places)
Constraints :
0 <= k <= 1000
Sample Input 1 :
3
Sample Output 1 :
1.87500
Sample Input 2 :
4
Sample Output 2 :
1.93750

'''


def GeomertricSum(n):
    if n ==0 :
        return 1

    sum = GeomertricSum(n-1)
    
    return 1/(2**(n)) + sum

def main():
    print('1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)')
    input_num = int(input('enter the value of k: '))
    sum = GeomertricSum(input_num)
    print(sum)

if __name__ =='__main__':
    main()
