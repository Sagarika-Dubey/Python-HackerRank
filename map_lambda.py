cube = lambda x: x ** 3 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibo = []
    for i in range(n):
        if i == 0:
            fibo.append(0)
        elif i == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))