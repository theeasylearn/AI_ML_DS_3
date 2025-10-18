#Arithmatic o:

num1=13
num2=45

addition=num1+num2
print(addition)
#o/p:58

subtraction=num2-num1
print(subtraction)
#32

multiplication=num1*num2
print(multiplication)
#585

division=num1/num2
print(division)
#0.28888888888888886

modulus=num1%num2
print(modulus)
#13

exponent=5**2
print(exponent)
#25

floordiv=num1//num2
print(floordiv)
#0

#conditional operators:

a=34
b=23
c=34

print(a==b)
print(a==c)#True

print(a!=b)#True
print(a!=c)

print(a<b)#False
print(a>b)#True

print(a<=b)#False
print(a>=b)#True
print(a<=c)#True
print(b>=c)#False

res1=a>=b and c<=a
print(res1)

res2=a>=b or c<=a
print(res2)
#t t t
#t f t
#f f f

print(not(a<=b or b>=c))
#Before not operator ans is False
#True

#Assignment operator:
print(c)
c=a+b
print(c)

c+=a
print(c)
#c=c+a
#91

c-=b
print(c)
#68

c*=2
print(c)
#136

c/=2
print(c)
#68.0

c**=2
print(c)
#4624.0

c//=20
print(c)
#231.0