import string
def print_rangoli(size):
    # your code goes here
    letters = string.ascii_lowercase[:size][::-1]
    width = 2* ( 2 * size -1)-1
    for i in range(size):
        print("-".join(letters[:i+1] + letters[:i][::-1]).center(width, "-"))
    for i in range(size,1, -1):
        print("-".join(letters[:i-1] + letters[:i-2][::-1]).center(width, "-"))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)