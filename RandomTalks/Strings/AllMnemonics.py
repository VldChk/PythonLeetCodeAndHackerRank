mapping = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"]
}


def calcMnemonics(s: list, n: int):
    res = list()
    for i in mapping[n]:
        for j in s:
            res.append(str(j) + str(i))
    return res


def allMnemonics(s: str):
    res = mapping[int(s[0])]
    for i in s[1::]:
        res = calcMnemonics(res, int(i))
    return res


print(len(allMnemonics("22233442")))