import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import pandas as pd
import numpy as np
from PIL import Image
import io
import os

wdir = "C:/Users/sm/Documents/GitHub/where-is-wally/src/data/img/64/"
waldos = np.array([np.array(imread(wdir + "waldo/"+fname)) for fname in os.listdir(wdir + "waldo")])
notwaldos = np.array([np.array(imread(wdir + "notwaldo/"+fname)) for fname in os.listdir(wdir + "notwaldo")])


##Append Flag Waldo to files with waldo
data = []
for im in waldos:
    data.append(im.flatten('F'))
    
df1 = pd.DataFrame(data)
df1['waldo'] = 1


##not waldo
data = []
for im in notwaldos:
    data.append(im.flatten('F'))
df2 = pd.DataFrame(data)
df2['waldo'] = 0

##Concatenate Files 
frames = [df1, df2]
allwaldos = pd.concat(frames)
#allwaldos.to_csv('"C:/Users/sm/Documents/GitHub/where-is-wally/src/data/all_waldo64.csv',index=False)

print(allwaldos)