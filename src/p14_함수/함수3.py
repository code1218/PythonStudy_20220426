customer = input('고객의 등급을 입력해주세요: ')
pay = int(input('상품의 금액을 입력해주세요: '))

def discount(_customer, _pay):
    _discountPay = 0

    if _customer == 'vip' :    
        _discountPay = _pay - (_pay * 0.3)
    elif customer == 'gold':
        _discountPay = _pay - (_pay * 0.2)
    elif customer == 'silver':
        _discountPay = _pay - (_pay * 0.1)
    else:
        _discountPay = _pay - (_pay * 0.05)
    
    return _discountPay

discountPay = int(discount(customer, pay))

print(f"{customer} 고객의 할인 적용된 금액은 {discountPay}입니다.")