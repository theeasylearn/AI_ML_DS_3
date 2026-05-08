# write a program to print following pattern 
'''
1 0 1 0 1
1 0 1 0
1 0 1
1 0
1 
'''
row = 5
while row>=1: #outer loop
    column = 1
    while column<=row: #inner loop 
        if column%2==1:
            print('1',end=' ')
        else:
            print('0',end=' ')
        column+=1
    print('') #new line
    row-=1

