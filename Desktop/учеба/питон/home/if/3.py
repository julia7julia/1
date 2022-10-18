price1 = int(input(''))
price2 = int(input(''))
price3 = int(input(''))
if price3>price2 and price2>price1:
    pay = (price1+price2+price3)/2
    print('Акция')
    print(pay)
elif price1>price2 and price2>price3:
    pay = (price1+price2+price3)/3
    print('Акция')
    print(pay)
else:
    pay = price1+price2+price3
    print(pay)
