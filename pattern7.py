'''
This is the patter code to print the '*'
using the recursion method as its shown 
in the below diagram,
* 
* * 
* * * 
* * * * 
* * * * * 
'''

def half_pyramid(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print('*', end=' ')
        print("")

if __name__ == '__main__':
    half_pyramid(5)