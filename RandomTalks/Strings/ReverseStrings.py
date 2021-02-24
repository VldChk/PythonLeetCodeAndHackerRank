def reverse_words(s: str):
    l = s.split(' ')
    s = str()
    for i in l[::-1]:
        s += i
        s += ' '

    return s

print(reverse_words('Alice likes Bob'))