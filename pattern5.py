'''
This is the patter code to print the '*'
using the recursion method as its shown 
in the below diagram,
*********
 *******
  *****
   ***
    *
'''
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(2*i - 1):
            print('*', end='')
        print()

inverted_pyramid(5)