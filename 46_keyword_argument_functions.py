def getMerit(maths,science,english,history,computer,drawing):
    print(f"maths={maths},science={science},english={english},history={history},computer={computer},drawing={drawing}")
    total = maths+science+english
    return total
m = int(input("Enter Maths marks: "))
s = int(input("Enter Science marks: "))
e = int(input("Enter English marks: "))
h = int(input("Enter History marks: "))
c = int(input("Enter Computer marks: "))
d = int(input("Enter Drawing marks: "))
print(getMerit(h,c,d,m,s,e)) #wrong way
print(getMerit(history=h,drawing=d,computer=c,maths=m,english=e,science=s)) #right way