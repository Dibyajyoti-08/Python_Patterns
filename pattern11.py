'''
Printing * pattern in a diamond shape
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
:param n: <int> number of rows to print the star in the above format
'''

def diamond_pattern(n):
    # Upper half of the pattern
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
    # Lower half of the pattern
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

diamond_pattern(5)