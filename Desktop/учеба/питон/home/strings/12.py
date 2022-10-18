#<span>5&nbsp;128&nbsp;P</span>
price=input('')
number=price.find('>')
number1=price.find('&')
a=price[number+1:number1]
#part1=int(a)
#print(part1)
number2=price.find(';')
number3=price.rfind('&')
b=price[number2+1:number3]
#part2=int(b)
#print(part2)
#print(a+b)
result=int(a+b)
print(result+1)


