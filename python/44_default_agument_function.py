#example of default argument function
def getSeconds(hours,minutes=0,seconds=0):
    print(f"hours = {hours} minutes = {minutes} seconds={seconds}")
    total_seconds = (hours * 3600) + (minutes * 60) + seconds 
    return total_seconds

# Accepting hours, minutes, and seconds as input
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = getSeconds(hours,minutes,seconds)
print(f" total seconds = {total_seconds}")

total_seconds = getSeconds(hours,minutes)
print(f" total seconds = {total_seconds}")

total_seconds = getSeconds(hours)
print(f" total seconds = {total_seconds}")