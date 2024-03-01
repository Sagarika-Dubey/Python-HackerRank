if __name__ == '__main__':
    s = input()
    is_alphanumeric = [any(i.isalnum() for i in s)]
    is_alphabetical = [any(i.isalpha() for i in s)]
    is_digit = [any(i.isdigit() for i in s)]
    is_lowercase = [any(i.islower() for i in s)]
    is_uppercase = [any(i.isupper() for i in s)]
    
    print(is_alphanumeric[0])
    print(is_alphabetical[0])
    print(is_digit[0])
    print(is_lowercase[0])
    print(is_uppercase[0])