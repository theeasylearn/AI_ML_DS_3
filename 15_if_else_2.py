'''
    write a program to findout whether shape is potrait or landscape using user given height and width 
'''
height = int(input("Enter height for shape"))
width = int(input("Enter width for shape"))
if height>width: # == != < > <= >=
    print("this is potrait shape")
else:
    print("this is landscape shape")