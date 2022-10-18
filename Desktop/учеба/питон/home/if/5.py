number = int(input(''))
number_str = str(number)
end = number_str[::-1][0]
a = int(end)
b = 0
while number != 0:
    b = b + number % 10
    number = number//10
if b % 3 == 0 and a % 2 == 0:
    print('делится на 6')
else:
    print('не делится на 6')
