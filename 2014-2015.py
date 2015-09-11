# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:15:41 2015

@author: Brian.McGuirk
"""
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats, integrate
import matplotlib.pyplot as plt

file = "C:\\Users\\brian.mcguirk\\dev\\random\\premier_league\\2014-2015.csv"
results = pd.read_csv(file)

results["GD"] = results["GF"] - results["GA"]
print(results)

sns.set(color_codes=True)
gd_set = results[["GD","Pos"]]
top_10 = gd_set.loc[:9]
print(top_10)

#sns.distplot(gd_set)

#points_gd = results[["Points","GD"]]


gd_pos = sns.jointplot(x=results["GD"],y=results["Pos"],color="b")

#sns.pairplot(results_data)

#sns.distplot(gd_set, bins=20)