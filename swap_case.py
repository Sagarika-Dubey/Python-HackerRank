def swap_case(s):
    word = []
    for _ in s:
        if _.isalpha():
            if _.islower():
                word.append(_.upper())
            elif _.isupper():
                word.append(_.lower())
        else:
            word.append(_)
    return ''.join(word)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)