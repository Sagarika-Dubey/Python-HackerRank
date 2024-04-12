def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    s=len(string)
    k_score=0
    s_score=0
    for i in range(s):
        if string[i] in vowels:
            k_score=k_score+(s-i)
        else:
            s_score=s_score+(s-i)
    if (k_score>s_score):
        print(f"Kevin {k_score}")
    elif (s_score>k_score):
        print(f"Stuart {s_score}")
    else:
        print("Draw")
         
if __name__ == '__main__':
    s = input()
    minion_game(s)