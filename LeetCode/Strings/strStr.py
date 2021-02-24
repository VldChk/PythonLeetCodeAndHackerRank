def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    elif len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            matched = True
            for j in range(1, len(needle)):
                if haystack[i + j] != needle[j]:
                    matched = False
                    break
            if matched:
                return i
    return -1