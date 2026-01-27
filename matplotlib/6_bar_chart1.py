import matplotlib.pyplot as plt
# India's Annual Two-Wheeler Domestic Sales (Approx. in Millions)
# Includes Motorcycles, Scooters, and Mopeds

years = list(range(2000, 2026))

# Sales figures in millions of units (approximate based on SIAM data)
two_wheeler_sales = [
    3.76,  # 2000
    4.27,  # 2001
    5.01,  # 2002
    5.62,  # 2003
    6.21,  # 2004
    7.05,  # 2005
    7.86,  # 2006
    8.03,  # 2007 (Impacted by interest rates)
    7.44,  # 2008 (Global recession impact)
    8.42,  # 2009
    10.51, # 2010 (Crossed the 10m mark)
    12.75, # 2011
    13.80, # 2012
    14.81, # 2013
    16.00, # 2014
    16.45, # 2015
    17.59, # 2016
    17.79, # 2017
    21.18, # 2018 (All-time high peak)
    17.42, # 2019 (Slowdown due to insurance/safety norms)
    15.12, # 2020 (Pandemic lockdowns)
    13.57, # 2021 (Supply chain & pandemic impact)
    15.86, # 2022 (Recovery phase)
    17.97, # 2023
    19.61, # 2024
    20.50  # 2025 (Crossed 2 crore mark again post-pandemic)
]

four_wheeler_sales = [
    0.16,  # 2000
    0.15,  # 2001
    0.19,  # 2002
    0.26,  # 2003
    0.33,  # 2004
    0.36,  # 2005
    0.47,  # 2006
    0.49,  # 2007
    0.42,  # 2008 (Global recession dip)
    0.53,  # 2009
    0.68,  # 2010 (Post-recession infrastructure push)
    0.81,  # 2011
    0.79,  # 2012
    0.63,  # 2013 (Stagnant economy)
    0.61,  # 2014
    0.69,  # 2015
    0.71,  # 2016
    0.86,  # 2017
    1.01,  # 2018 (Historical peak before the 2025 record)
    0.72,  # 2019 (Slowdown + BS-VI transition)
    0.57,  # 2020 (Pandemic impact)
    0.72,  # 2021
    0.96,  # 2022 (E-commerce & Infra boom)
    0.97,  # 2023
    0.96,  # 2024
    1.03   # 2025 (New All-time high record)
]
plt.figure(figsize=(15,10))
plt.bar(years,two_wheeler_sales,width=0.3,color='blue',edgecolor='black')
plt.bar(years,four_wheeler_sales,width=0.3,color='yellow',edgecolor='red')
plt.xlabel('years')
plt.ylabel('Sales in Millions')
plt.title('Vehicle sales data')
plt.ylim(0,25)
plt.grid(True)
plt.show()