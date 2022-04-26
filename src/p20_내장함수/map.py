def madeNickName(name):
    return name + "님"

names = ["김준일", "전주홍", "김가람", "이진서"]

print(list(map(madeNickName, names)))