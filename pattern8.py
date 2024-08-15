'''
This is the pattern code to print the numbers
which will be in the half pyramid pattern,
1 
1 2 
1 2 3
1 2 3 4 
1 2 3 4 5
'''
def half_number_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j,end=" ")
        print()

if __name__ == '__main__':
    half_number_pyramid(5)