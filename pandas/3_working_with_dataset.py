import pandas as pd 
import connection as con 
#create series 
# s1 = pd.read_csv('marks.csv').squeeze()
# print(s1)
# s2 = pd.read_excel('marks.xlsx').squeeze()
# print(s2)
# s3 = pd.read_json('marks.json').squeeze()
# print(s3)
sql = "select productcode, productname, productline from products"
s4 = pd.read_sql(sql,con.database).squeeze()
print(s4)