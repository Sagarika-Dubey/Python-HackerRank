def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    prev = 0
    t = k
    while t <= l:
        cur = ""
        for i in range(prev,t):
            if string[i] not in cur:
                cur+=string[i]
        prev = t
        t += k
        print(cur)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)