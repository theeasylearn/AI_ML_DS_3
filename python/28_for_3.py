#working with for loop and tuples 
numbers = (-347, 512, -890, 233, 768, -92, 405, -731, 999, -12, 674, -583, 218, 904, -440, 156, -999, 782, 63, -415, 358, -664, 120, 715, -276, 844, -187, 507, -943, 311, 97, -512, 421, -805, 259, 688, -344, 916, -721, 532, -9, 867, -623, 178, -459, 234, -775, 614, 382, -398, 901, -128, 700, -687, 247, 466, -310, 593, -850, 475, 208, -214, 663, -932, 581, -98, 347, 773, -289, 459, -678, 242, 831, -566, 149, 693, -412, 888, -331, 603, 195, -702, 548, -275, 879, -493, 377, -841, 212, -124, 965, -305, 487, -999, 601, -72, 825, -633, 274, 319)

negative = 0
positive = 0 

for num in numbers: #512
    if num<0:
        negative=negative+1
    else:
        positive=positive+1

print(f"No of negative values = {negative}")
print(f"No of positive values = {positive}")

# count all odd values & even values & values divisble by 10 
# sum of all negative and sum of all positive values 
# sum of all values 