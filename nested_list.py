if __name__ == '__main__':
    students = []
    scores = []
    second_low_st = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
        scores.append(score)
    
    scores.sort()

    lowest_score = scores[0]
    second_lowest = scores[1]  
    i = 2
    
    while (second_lowest == lowest_score): 
        second_lowest = scores[i]
        i += 1 
        
    for student in students:
        if student[1] == second_lowest:
            second_low_st.append(student[0])
        
    second_low_st.sort()
    print ('\n'.join(second_low_st))