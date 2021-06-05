# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:47:33 2021

@author: navaneethsharma2310
"""

import glob
from PIL import Image 
import numpy as np
import pandas as pd



folder_names = glob.glob("training_dataset\\*")
label = []
data = []
for folder in folder_names:
    filenames = glob.glob(folder+'\\*')
    
    for file in filenames:
        
        label = label+[[folder.split('\\')[1]]]
        img = Image.open(file).convert('RGB')
        img = img.resize((28,28))     
        img1 = np.asarray(img)   
        img1 = img1.reshape(-1,)
        
        data.append(img1)
        
df1 = pd.DataFrame(data,columns=[str(i) for i in range(28*28*3)])
df2 = pd.DataFrame(label,columns=['label'])

df = df1.join(df2)

df.to_csv('C:\\Users\\navaneethsharma2310\\Desktop\\color_data.csv')

