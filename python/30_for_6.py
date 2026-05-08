#for loop with nested dictionary
teams = {
    "India": {"Rohit":78, "Gill":45, "Kohli":92, "Iyer":36, "Rahul":58, "Hardik":24, "Jadeja":41, "Ashwin":15, "Shami":10, "Bumrah":5, "Siraj":8},
    "Australia": {"Warner":82, "Head":66, "Smith":90, "Labuschagne":55, "Maxwell":47, "Green":38, "Carey":29, "Starc":15, "Cummins":11, "Zampa":7, "Hazlewood":9},
    "England": {"Buttler":75, "Bairstow":62, "Root":88, "Brook":59, "Stokes":72, "Livingstone":33, "Moeen":25, "Rashid":18, "Archer":10, "Wood":8, "Curran":12},
    "Pakistan": {"Babar":95, "Rizwan":68, "Fakhar":77, "Imam":54, "Saud":42, "Shadab":29, "Nawaz":22, "Shaheen":13, "Haris":11, "Naseem":9, "Rauf":7},
    "New Zealand": {"Conway":81, "Allen":64, "Williamson":93, "Mitchell":70, "Phillips":56, "Chapman":41, "Santner":28, "Southee":16, "Boult":10, "Ferguson":8, "Henry":12},
    "South Africa": {"Bavuma":67, "De_Kock":88, "Markram":73, "Miller":69, "Klaasen":84, "Jansen":35, "Maharaj":21, "Rabada":14, "Ngidi":10, "Nortje":9, "Coetzee":11},
    "Sri Lanka": {"Nissanka":72, "Kusal":59, "Mendis":80, "Asalanka":64, "Mathews":45, "Shanaka":39, "Hasaranga":33, "Theekshana":17, "Pathirana":12, "Chameera":8, "Madushanka":10},
    "Bangladesh": {"Litton":63, "Tamim":71, "Shanto":77, "Mushfiqur":66, "Mahmudullah":48, "Hridoy":36, "Mehidy":28, "Taskin":13, "Mustafizur":9, "Shoriful":8, "Hasan":10},
    "Afghanistan": {"Gurbaz":74, "Ibrahim":68, "Shahidi":82, "Rahmat":55, "Nabi":44, "Omarzai":37, "Rashid":31, "Mujeeb":18, "Naveen":11, "Farooqi":9, "Noor":7}
}
print(teams['india']['rohit'])
print(teams['Australia']['Warner'])
for team in teams:
    print(team)
    for player in teams[team]:
        print(f"{player} = {teams[team][player]}")
    print("-"*100)

#findout team wise total and findout which team has made maximum runs 
#findout team wise total and findout which team has made minimum runs 