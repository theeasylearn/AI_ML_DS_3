# write a program to findout whether two person can donate blood to each other or not using given both person's blood group 
#complete remaining blood group matching as per below chart 
# https://stanfordbloodcenter.org/wp-content/uploads/2018/03/0318-SouthBay-Center-Infographics_Compatibility-WEB-250x230.jpg
donor = input("Enter blood group of donor")
receiver = input("Enter blood group of receiver")

if donor=='o+' and (receiver=='o+' or receiver=='o-'):
    print(f"donor {donor} can give blood to receiver {receiver}")
elif donor==receiver and donor=='o-':
    print(f"donor {donor} can give blood to receiver {receiver}")
elif donor=='a+' and (receiver=='o+' or receiver=='o-' or receiver=='a+' or receiver=='a-'): 
    print(f"donor {donor} can give blood to receiver {receiver}")