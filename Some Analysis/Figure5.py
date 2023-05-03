
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

df_confidence=pd.read_excel('Assignment 2.xlsx',
    sheet_name='Figure 5')
df_confidence['Periods'] = pd.to_datetime(df_confidence['Periods'])
print(df_confidence.dtypes )
print(df_confidence)


plt.rc('font', size=18)
fig, ax = plt.subplots(figsize=(18,24))
# Specify how our lines should look
ax.plot(df_confidence['Periods'],
    df_confidence['Consumer confidence'],
    color='red', label='Consumer confidence') 

ax.plot(df_confidence['Periods'],
df_confidence['Economic climate'] ,color='blue', label='Economic climate')

ax.plot(df_confidence['Periods'],
df_confidence['Willingness to buy'] ,color=GREEN, label='Willingness to buy ')


ax.set_ylabel('Average of Answers [-100,100]')
# Make gridlines be below most artists.
ax.set_axisbelow(True)

# Add grid lines
ax.grid(axis = "y", color="#A8BAC4", lw=1.2)
# Add labels for vertical grid lines -----------------------
# The pad is equal to 1% of the vertical range (35 - 0)
PAD = 18 * 0.01
for label in [i * 5 for i in range(0, 7)]:
    ax.text(
        2021.5, label + PAD, label, 
        ha="right", va="baseline", fontsize=14,
        fontfamily="Econ Sans Cnd", fontweight=100
    )

ax.legend(loc='upper right');
plt.xticks(rotation = 90) 
plt.show()