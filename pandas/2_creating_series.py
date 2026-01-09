import numpy as np 
import pandas as pd 

list = [100,200,250]
s1 = pd.Series(list,name='data-set-1')
print(s1)
array1 = np.array(list) #create array using numpy 
#create list using numpy array
s2 = pd.Series(array1,name='data-set-2')
print(s2)
virat_kohli_odi_centuries = {
    "24 December 2009": "107",
    "11 January 2010": "102*",
    "20 October 2010": "118",
    "28 November 2010": "105",
    "19 February 2011": "100*",
    "16 September 2011": "107",
    "17 October 2011": "112*",
    "2 December 2011": "117",
    "28 February 2012": "133*",
    "13 March 2012": "108",
    "18 March 2012": "183",
    "21 July 2012": "106",
    "31 July 2012": "128*",
    "5 July 2013": "102",
    "24 July 2013": "115",
    "16 October 2013": "100*",
    "30 October 2013": "115*",
    "19 January 2014": "123",
    "26 February 2014": "136",
    "17 October 2014": "127",
    "16 November 2014": "139*",
    "15 February 2015": "107",
    "22 October 2015": "138",
    "17 January 2016": "117",
    "20 January 2016": "106",
    "23 October 2016": "154*",
    "15 January 2017": "122",
    "6 July 2017": "111*",
    "31 August 2017": "131",
    "3 September 2017": "110*",
    "22 October 2017": "121",
    "29 October 2017": "113",
    "1 February 2018": "112",
    "7 February 2018": "160*",
    "16 February 2018": "129*",
    "21 October 2018": "140",
    "24 October 2018": "157*",
    "27 October 2018": "107",
    "15 January 2019": "104",
    "5 March 2019": "116",
    "8 March 2019": "123",
    "11 August 2019": "120",
    "14 August 2019": "114*",
    "10 December 2022": "113",
    "10 January 2023": "113",
    "15 January 2023": "166*",
    "10 September 2023": "122*",
    "19 October 2023": "103*",
    "5 November 2023": "101*",
    "15 November 2023": "117"
}
#create series using dictionary
s3 = pd.Series(virat_kohli_odi_centuries,name='data-set-3')
print(s3)