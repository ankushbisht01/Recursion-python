'''
Chapter Assignment
Problem Statement: Staircase
Problem Level: EASY
Problem Description:
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
Input format :
Integer N

Output Format :
Integer W
'''

def staircase(n):
    
    if n==3:
       return 3
    if n==2:
        return 2
    if n ==1:
       return 1

    x = staircase(n-1) 
    y = staircase(n-2)  
    z = staircase(n-3)
    
    
    return x +y + z 
   
       
def main():
    no_of_stairs = int(input('enter the number of stair case :'))
    pos_way_to_climb = staircase(no_of_stairs)
    print('possible ways to climb the {0} stairs are {1}'.format(no_of_stairs,pos_way_to_climb) )

if __name__ =='__main__':
    main()