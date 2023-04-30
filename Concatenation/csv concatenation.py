import pandas as pd

i = 0

while i < 36:
    
    if i == 4:
        d0 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/4/0.csv".format(i))
        d2 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/4/2.csv".format(i))
        d3 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/4/3.csv".format(i))
        
        data = pd.concat([d0, d2, d3])
        
        data.to_csv("4.csv")
        
        i = i + 1
        
    d0 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/{}/0.csv".format(i))
    d1 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/{}/1.csv".format(i))
    d2 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/{}/2.csv".format(i))
    d3 = pd.read_csv("C:/Users/Jack/Desktop/S&S Map/Concatenation/Wales S&S Data/{}/3.csv".format(i))
    
    data = pd.concat([d0, d1, d2, d3])
    
    data.to_csv("{}.csv".format(i))
    
    i = i + 1