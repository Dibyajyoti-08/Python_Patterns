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

def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)


def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)


def print_pyramid(n, current_row=1):
    if current_row > n:
        return
    
    space = n - current_row
    star = 2 * current_row - 1

    print_space(space)
    print_star(star)

    print()

    print_pyramid(n, current_row + 1)

if __name__ == '__main__':
    n = 5
    print_pyramid(5)
