if __name__ == '__main__':
    N = int(input())
    user_list = []
    
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            user_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(user_list)
        elif command[0] == "remove":
            user_list.remove(int(command[1]))
        elif command[0] == "append":
            user_list.append(int(command[1]))
        elif command[0] == "sort":
            user_list.sort()
        elif command[0] == "pop":
            user_list.pop()
        elif command[0] == "reverse":
            user_list = user_list[::-1]