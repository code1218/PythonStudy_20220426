def namesAndphones(names, phones):
    namesStr = "||".join(names)
    phonesStr = "|".join(phones)
    return namesStr, phonesStr

names = ["김준일","송지한","이건용","이영헌","전주홍"]
phones = ["010-9988-19196","010-9988-19196","010-9988-19196","010-9988-19196","010-9988-19196"]
result = namesAndphones(names, phones)
result1, result2 = namesAndphones(names, phones)
print(result)
print(result1)
print(result2)
