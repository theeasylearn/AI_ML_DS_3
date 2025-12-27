#import currency module
import currency 
rs = int(input("Enter rupees to convert it into different currencies "))

dollar = currency.toDollar(rupees=rs)
pound = currency.toPound(rupees=rs)
euro = currency.toEuro(rupees=rs)

print(dollar)
print(pound)
print(euro)