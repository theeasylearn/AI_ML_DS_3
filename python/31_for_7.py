# nested list
delhi_aqi = [
    [145, 210, 189, 320, 275, 410, 380],  # Week 1
    [260, 305, 330, 285, 410, 395, 370],  # Week 2
    [420, 385, 440, 310, 295, 260, 355],  # Week 3
    [280, 360, 340, 455, 380, 410, 290],   # Week 4
    [300,400],   # Week 5
]
# findout average aqi
count = 0
total = 0 
for week in delhi_aqi: #outer for loop
    #print(week)
    for item in week:
        #print(item)
        total = total + item 
        count = count + 1
    
#average calculate 
average = total / count 
print(f"total = {total} count = {count} average = {average}")

#display days less then average aqi and also count it 
less_then_average_count = 0
for week in delhi_aqi:
    for item in week:
        if item<average:
            print(item)
            less_then_average_count= less_then_average_count + 1

print(f"total no days where aqi is less then average = {less_then_average_count}")

#findout minimum and maximum aqi 
#findout week whose average is least  other week average
#findout week whose average is maximum  other week average

