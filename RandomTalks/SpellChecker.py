import sys

words = ['cat', 'bat', 'rat', 'drat', 'dart', 'drab']


def isMatched(s):
    tmp_words = words
    is_Matched = False
    for word in words:
        if word.__len__() == s.__len__():
            curr_word = True
            for i in range(word.__len__()):
                if word[i] != s[i] and s[i] != '.':
                    curr_word = False
                    break
            if curr_word is True:
                is_Matched = True
                return is_Matched
        else:
            continue
    return is_Matched


for line in sys.stdin:
    print(isMatched(line))