'''
This is the patter code to print the numbers
from 1 to 5 as its shown in the below diagram,
1
12
123
1234
12345
'''

num = 1
def solve(n):
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end='')
            num += 1
        print("")

if __name__ == '__main__':
    solve(5)