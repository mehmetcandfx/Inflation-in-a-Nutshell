
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from numpy import log as ln
import numpy as np
import math
from flexitext import flexitext

from matplotlib import lines
from matplotlib import patches
from matplotlib.patheffects import withStroke

BROWN = "#AD8C97"
BROWN_DARKER = "#7d3a46"
GREEN = "#2FC1D3"
BLUE = "#076FA1"
GREY = "#C7C9CB"
GREY_DARKER = "#5C5B5D"
RED = "#E3120B"

df_Inf_Wage=pd.read_excel('Assignment 2.xlsx',
    sheet_name='Figure 4')
df_Inf_Wage['Periods'] = pd.to_datetime(df_Inf_Wage['Periods'])
print(df_Inf_Wage.dtypes )
print(df_Inf_Wage)


plt.rc('font', size=18)
fig, ax = plt.subplots(figsize=(18,24))

# Specify how our lines should look
ax.plot(df_Inf_Wage['Periods'],
    df_Inf_Wage['Monthly Cao wages'],
    color='orange', label='Monthly wages') 

ax.plot(df_Inf_Wage['Periods'],
df_Inf_Wage['CPI (%)'] ,color='red', label='HICP ')
ax.set_ylabel('YoY Change (%)')
ax.set_axisbelow(True)

# Add grid lines
ax.grid(axis = "y", color="#A8BAC4", lw=1.2)
ax.grid(axis = "x", color="#A8BAC4", lw=1.2)
# Add labels for vertical grid lines -----------------------
# The pad is equal to 1% of the vertical range (35 - 0)
PAD = 18 * 0.01
for label in [i * 5 for i in range(0, 7)]:
    ax.text(
        2021.5, label + PAD, label, 
        ha="right", va="baseline", fontsize=14,
        fontfamily="Econ Sans Cnd", fontweight=100
    )

ax.legend(loc='upper left');

plt.xticks(rotation = 90) 
plt.show()