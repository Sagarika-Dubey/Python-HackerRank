def print_formatted(number):
    # your code goes here
    w = len(str(bin(n))[2:])
    for i in range(1,n+1):
        print(str(i).rjust(w,' '),
            (oct(i))[2:].rjust(w,' '),
            (hex(i)).upper()[2:].rjust(w,' '), # upper
            (bin(i))[2:].rjust(w,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)