number = -1

try:
    if number > 0:
        pass
    elif number == -1:
        list1 = [1,2,3,4,5]
        list1.index(6)        
    else:
        raise FileNotFoundError
except ValueError as e:
    print(f"오류 내용: {e}")
except IndexError as e:
    print(f"오류 내용: {e}")
except FileNotFoundError as e:
    print(f"오류 내용: {e}")
except Exception as e: # 항상 마지막에 있어야함
    import traceback
    traceback.print_exc()
else:
    print("오류가 발생하지 않으면 실행")
finally:
    print("무조건 실행")

print("프로그램 종료")

