a=int(input())
for i in range(0,a):
    b,c=map(str,input().split())
    try:
        div=int(b)/int(c)
        print("{:.0f}".format(div))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
