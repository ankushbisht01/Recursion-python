'''
Question - 
create a function to count the number of digit in the given input using recursion

Sample input - 
1234
Sample output -
4
'''

def count(n):
    n = abs(n)
    if n //10 ==0 :
        return 1
    digits_count = count(n//10)
    return digits_count+1

print(count())