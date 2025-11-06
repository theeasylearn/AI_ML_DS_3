# write a program that display countries ends with land
countries = ["Uzbekistan", "Sweden", "Thailand", "Kazakhstan", "Poland", "Egypt", "Afghanistan", "Greenland", "France", "Iceland", "Tajikistan", "Denmark", "Australia", "Switzerland", "Pakistan", "Norway", "Kyrgyzstan", "Ireland", "Germany", "Netherlands", "India", "Canada", "Japan", "Spain", "Mexico", "Finland", "Brazil", "China", "Turkmenistan", "Italy",'India','Japan']

# display countries ends with land
for country in countries:
    if "land" in country:
        print(country)
print("_"*100)
# display countries ends with stan
for country in countries:
    if "stan" in country:
        print(country)

# display those coutries which does not ends with stan and land 