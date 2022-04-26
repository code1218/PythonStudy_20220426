point = 280

if point > 899:
    print("VIP회원")
else:
    if point > 799:
        print("GOLD회원")
    else:
        if point > 699:
            print("SILVER회원")
        else:
            if point > 499:
                print("BRONZE회원")
            else:
                print("일반회원")

if point > 899:
    print("VIP회원")

elif point > 799:
    print("GOLD회원")

elif point > 699:
    print("SILVER회원")

elif point > 499:
    print("BRONZE회원")
else:
    print("일반회원")
