if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    x = student_marks[query_name] 
    avg = sum(x)/len(x) 
    avg_f = format(avg, '.2f') 
    print(avg_f)