if __name__ == "__main__":
    sizeM = int(input())
    M = set(map(int, input().split()))
    sizeN = int(input())
    N = set(map(int, input().split()))
    
    if len(M) == sizeM and len(N) == sizeN:
        diff = M.difference(N)
        diff.update(N.difference(M))
        
        for i in sorted(diff):
            print(i)
    else: print('Error in parameters')