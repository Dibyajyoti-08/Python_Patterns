'''
This is the patter code to print the '*'
as its shown in the below diagram,
    *
   ***
  *****
 *******
*********
'''

def solve(n):
    for i in range(1, n+1):
        # The j loop is for the leading spaces 
        for j in range(n - i):
            print(' ', end='')
        # The k loop is for the printing of '*'
        for k in range(1, 2*i):
            print("*", end='')
        print()

if __name__ == '__main__':
    solve(5)