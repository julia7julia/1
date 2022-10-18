good = input('')
if good == 'продукты':
    print('укажите цену')
    price = int(input(''))
    if price < 100:
        print('Попробуйте нашу выпечку!')
    elif price >=100 and price < 500:
        print('Как насчет орехов в шоколаде?')
    elif price >=500:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')
