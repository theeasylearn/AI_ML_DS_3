# write a program to print following pattern 
'''
*
* *
* * *
* * * *
* * * * *
'''
for row in range(1,6):
    for astrik in range(0,row): #1 2 3 4 5
        print('*',end=' ')
    print('') #new line
