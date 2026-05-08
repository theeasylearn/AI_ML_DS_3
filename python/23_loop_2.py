# write a program to print below sequence 
# 0 1 1 2 3 5 8 13 21 .... 100
#       p c n
#       p c 
prev = 0 
cur = 1

print(prev)
print(cur)

while cur<89:
    next = prev + cur #1 
    print(next)
    prev = cur 
    cur = next

