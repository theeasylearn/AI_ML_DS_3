'''
    *
   **
  ***
 ****
*****

'''
raw=int(input("Enter number of raws:"))
for i in range(1,raw+1):
    
    for col in range(i,0,-1):#(1,5)/(1,4)/(1,3)...0
        print("*",end=' ')                                                 
    print( )