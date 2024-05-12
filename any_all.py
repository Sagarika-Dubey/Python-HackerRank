n= int(input())
lst = list(map(int,input().split()))
print(all([all(map(lambda x: x > 0 , lst)),any(map(lambda x: str(x) == str(x)[::-1] , lst))]))