#count함수
name = "김기덕"

nameStrCount = name.count('김')

print(f"문자 김의 개수: {nameStrCount}")

#find함수
address = "부산광역시 해운대구 송정동 송정중앙로"
print("find")
city = address.find("시")
print(address[:city+1])
#index함수
print("index")

cityIndex = address.index("시")
print(address[:city+1])

guIndex = address.find("구")
dongIndex =address.find("동")

print(address[cityIndex + 2:guIndex+1])
print(address[guIndex + 2:dongIndex+1])

roIndex = address.find("로")
print(address[roIndex +2:roIndex+1])

#join함수(문자열 삽입)
name = "김기덕"
nameJoin = "----".join(name)
print(nameJoin)

#upper(대문자변환)
str1 = "kideok"
print(str1.upper())

#lower(소문자변환)
str2 = str1.upper()
print(str2.lower())

#strip(공백제거)
username = " asdqwebnm "
lstripUsername = username.lstrip()
print("000" + lstripUsername + "000")

rstripUsername = username.rstrip()
print("000" + rstripUsername + "000")

stripUsername = username.strip()
print("000" + stripUsername + "000")

#replace(문자열 바꾸기)
phoneNumber = "010 4460 0980"
replacePhone = phoneNumber.replace("-", "")
replacePhone = replacePhone.replace(" ", "")
print(replacePhone)