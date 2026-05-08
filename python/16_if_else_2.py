'''
    write a program to help user to findout which is cheaper to product to purchase. user has 2 product's price and weight (in grams)
    Product A Price 1000 Weight 1000 grams price per gram 1000/1000 1 Rs
    Product B Price 500 Weight 400 grams price per gram 500/400 1.25 Rs
'''
price1 = int(input("Enter price for 1st product"))
weight1 = int(input("Enter weight for 1st product"))

price2 = int(input("Enter price for 1st product"))
weight2 = int(input("Enter weight for 1st product"))

#calcuate price per gram 
price_per_gram1 = price1/weight1
price_per_gram2 = price2/weight2 

print("1st product Price per gram =",price_per_gram1)
print("2nd product Price per gram =",price_per_gram2)

#findout cheaper product 
if price_per_gram1<price_per_gram2: # == != < > <= >=
    print("1st product is cheaper ",price_per_gram2 - price_per_gram1, " Rs per gram")
else:
    print("2nd product is cheaper ",price_per_gram1 - price_per_gram2, " Rs per gram")