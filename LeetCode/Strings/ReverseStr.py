# The simplest way in Python to do so is the next:

def reverse_str_simple(s: str) -> str:
    return s[::-1]


# If we try to right it on our own then we can for instance make it through list:
def reverse_str_list(s: str) -> str:
    l = list(s)
    n = len(s)
    for i in range(n//2):
        l[i], l[n-i-1] = l[n-i-1], l[i]
    return ''.join(l)


# Or though str:
def reverse_str(s: str) -> str:
    res = ''
    n = len(s)
    for i in range(n):
        res += s[n-i-1]
    return res


print(reverse_str('abcd'))
print(reverse_str_list('abcd'))
print(reverse_str_simple('abcd'))