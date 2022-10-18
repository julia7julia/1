#дорогие друзья, для связи со мной почта mymail@mymail.ru на личном сервере
string=input('')
symbol=string.find('@')
start=string.index(string)
#print(start)
a=string.rfind(' ', start, symbol)
b=string.find(' ', symbol, len(string))
#print(a)
#print(b)
mail=string[a+1:b:]
print(mail)