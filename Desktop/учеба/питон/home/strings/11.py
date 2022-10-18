#<a href='tel:+790123456'>+790123456</a>
#number=input('')
#add1='#<a href='tel:'
#add2=''>'
#add3='</a>'
#print(add1+number+add2+number+add3)

number=input('')
phone="<a href='tel: '> </a>"
print(phone.replace(' ', number))

