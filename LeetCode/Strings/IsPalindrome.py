def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


print(isPalindrome("0P"))