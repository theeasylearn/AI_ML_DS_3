import mplfinance as mpf 
import pandas as pd 
import numpy as np 
date = pd.date_range('2026-02-09',periods=5)
print(date)
data = pd.DataFrame({
    'date':date,
    'open'  : [84177.51, 84210.00, 84339.15, 83968.43, 82902.73],
    'high'  : [84314.68, 84482.95, 84487.34, 84061.62, 83079.70],
    'low'   : [83860.42, 84063.47, 84081.25, 83516.67, 82534.55],
    'close' : [84065.75, 84273.92, 84233.64, 83674.92, 82626.76]
})
data.set_index("date",inplace=True)
mpf.plot(data,type='candle',style='binance')
'''
Style Name,     Description
'binance',      Dark background with yellow/white accents; very popular for crypto.
'charles',      The classic look: White background with Green (Up) and Red (Down) candles.
'classic',      Mimics the old-school Matplotlib look.
'mike',         "Dark background with thin, high-contrast borders."
'nightclouds',   A unique dark blue/gray aesthetic.
'sas',          "Professional, clean gray-scale style often used in reports."
'yahoo',        The familiar look of Yahoo Finance charts (Green/Red).
'''