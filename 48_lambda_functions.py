toDollar = lambda rupees : rupees/92
getArea = lambda length,width : length * width 
getCyclienderArea = lambda radius,height : 3.14 * radius * radius * height
getMax = lambda a,b : a if a>b else b
rupees = float(input("Enter amount in rupees: "))
length = float(input("Enter length: "))
width = float(input("Enter width: "))
height = float(input("Enter height: "))
radius = float(input("Enter radius: "))

print(toDollar(rupees))
print(getArea(length,width))
print(getCyclienderArea(radius,height))
print(getMax(length,width))