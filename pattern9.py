'''
This is the pattern code to print the characters
which will be in the half pyramid pattern,
A 
B B 
C C C 
D D D D 
E E E E E 
'''
def char_half_pyramid(n):
    alph = 65
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(alph), end=" ")
        alph += 1
        print()

if __name__ == '__main__':
    char_half_pyramid(5)
