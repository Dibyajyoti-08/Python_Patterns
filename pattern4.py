'''
This is the patter code to print the alphabets
as its shown in the below diagram,
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 
'''
def pattern(n, alph):
    for i in range(0, n):
        print(" " * (n-i), end=" ")
        for j in range(0, i+1):
            print(chr(alph), end=" ")
            alph += 1
        alph = 65
        print()
if __name__ == '__main__':
    pattern(5, 65)



