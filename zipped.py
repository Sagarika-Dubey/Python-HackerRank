n, x= map(int, input().split())
student_marks=[]
for i in range(x):
    a=list(map(float, input().split(" ")))
    student_marks.append(a)
    
student_avg=[sum(x)/len(x) for x in zip(*student_marks)]
for i in student_avg:
    print(i)