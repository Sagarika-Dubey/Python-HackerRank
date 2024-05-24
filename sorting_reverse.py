def custom_sort_key(c):
    if c.islower():
        return (0, c)
    if c.isupper():
        return (1, c)
    if c.isnumeric():
        if int(c) % 2 == 1:
            return (2, c)
        else:
            return (3, c)
    
print("".join(sorted(list(input()), key=custom_sort_key)))
