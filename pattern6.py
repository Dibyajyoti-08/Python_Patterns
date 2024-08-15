'''
This is the patter code to print the '*'
using the recursion method as its shown 
in the below diagram,
    *    
   * *   
  *   *  
 *     * 
*********
'''
def hollow_pyramid(n):
    for i in range(1,n+1):
        for j in range(1, 2*n):
            if j == n-i+1 or j == n+i-1 or i==n:
                print('*', end='')
            else:
                print(' ', end='')
        print()

if __name__ == '__main__':
    n = 5
    hollow_pyramid(n)