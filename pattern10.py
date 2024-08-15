'''
This is the pattern code to print the *
which will be in the half pyramid pattern
in reverse format,
* * * * *
* * * *
* * *
* *
*
'''

def half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print('*', end=" ")
        print("\r")

if __name__ == '__main__':
    half_pyramid(5)

'''
Using recursion method to print the * in the below format,
* 
* * 
* * * 
* * * * 
* * * * * 
:param rows: <int> Number of rows the star pattern has to print
'''
def print_half_pyramid(rows):
    if rows > 0:
        print_half_pyramid(rows - 1)
        print('* ' * rows)

print_half_pyramid(5)