# numbers = [12, 45, 7, 89, 34, 56, 23, 78, 91, 10, 64, 38, 72, 5, 99, 41, 27, 83, 16, 60]
numbers = [12, 45, 7, 89, 34,'Mahi', 56, 23, 78, 91, 10, 64, 38, 72, 5, 99, 41, 27, 83, 16, 60]
sum = 0 
count = 0
for item in numbers:
    # print(item,end=' ')
    try:
        sum = sum  + item 
        count = count + 1
    except TypeError:
        print('invalid value skipped ',item)

average = sum / count
print(f"sum = {sum} average = {average}")