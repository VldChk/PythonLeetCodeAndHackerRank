def plusOne(digits: list) -> list:
    for i in range(len(digits)):
        digits[len(digits) - i - 1] = (digits[len(digits) - i - 1] + 1) % 10
        if digits[len(digits) - i - 1] == 0:
            continue
        else:
            return digits
    one = [1]
    one.extend(digits)
    return one

print(plusOne([9]))