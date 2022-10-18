# x = input()
# print(x[::-1])
#x=451
#a=x%10
#x=x//10
#b=x%10
#x=x//10
#c=x%10
#print(a*100+b*10+c)
x=int(input())
a=x//100
b=x%100//10
c=x%10
print(c*100+b*10+a)