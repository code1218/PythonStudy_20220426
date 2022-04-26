strName = "김준일, 김기덕, 송지한, 전주홍"

print(strName.find("김기덕"))

print(strName.find("노신비"))
try:
    print(strName.index("노신비"))
except:
    print("예외가 발생하였습니다.")
    
print("프로그램 정상 종료")