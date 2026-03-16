#Poornima Nedumpurath
#USDA Coding Test

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#READ EXCEL SHEETS
df = pd.read_excel("Coding_Test.xlsx", sheet_name="Oct", header=None)
df_nov = pd.read_excel("Coding_Test.xlsx", sheet_name="Nov", header=None)

#HELPER FUNCTIONS
def get_commodity(df, name, count):
    start = df[df[0] == name].index[0] + 1
    block = df.iloc[start:start + count]
    countries = block[0].values
    data_2024 = block[1].values
    data_2025 = block[2].values
    return countries, data_2024, data_2025

def get_commodity_nov(df, name, count):
    start = df[df[0] == name].index[0] + 1
    block = df.iloc[start:start + count]
    countries = block[0].values
    data_2024 = block[1].values
    return countries, data_2024

#OCTOBER DATA
#collect countries for each commodity
soy_countries, s2024, s2025 = get_commodity(df, "Soybeans", 10)
corn_countries, c2024, c2025 = get_commodity(df, "Corn", 10)
wheat_countries, w2024, w2025 = get_commodity(df, "Wheat, unmilled", 11)

#set up layout (october window)
fig = plt.figure(figsize=(10, 6))
fig.suptitle("Exports for Soybeans, Corn, and Wheat (Jan - Oct, 2024 and 2025)", fontsize=14)

ax1 = plt.subplot(2, 2, 1) #soybeans graph
ax2 = plt.subplot(2, 2, 2) #corn graph
ax3 = plt.subplot(2, 1, 2) #wheat graph

#Soybeans - Horizontal Bar Graph
soy_countries = soy_countries[::-1]
s2024 = s2024[::-1]
s2025 = s2025[::-1]

y = np.arange(len(soy_countries))
ax1.invert_yaxis() #format so its the same as given graph
ax1.barh(y, s2024, label="2024") #2024 data first
ax1.barh(y, s2025, left=s2024, label="2025") #2025 data stacks on top
#set up graph
ax1.set_yticks(y)
ax1.set_yticklabels(soy_countries)
#display numbers in full form
ax1.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax1.tick_params(axis='x', labelsize=6) #format x axis labels
ax1.set_title("Soybeans")
ax1.legend()

# Corn - Vertical Bar Graph
x = np.arange(len(corn_countries)) #countries on x axis
width = 0.35 #set width of bars
ax2.bar(x - width / 2, c2024, width, label="2024")
ax2.bar(x + width / 2, c2025, width, label="2025") #labels
#set up graph
ax2.set_xticks(x) #coutntries on x
ax2.set_xticklabels(corn_countries, rotation=65, fontsize=7)
#display numbers in full form
ax2.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax2.tick_params(axis='y', labelsize=6) #format y axis labels
ax2.set_title("Corn")
ax2.legend()

# Wheat - Line Graph
years = [2024, 2025]
for i in range(len(wheat_countries)): #for each country, plot data for 2024 and 2025
    ax3.plot(years, [w2024[i], w2025[i]], marker='o', label=wheat_countries[i])
ax3.set_xticks(years) #years on x axis
ax3.set_title("Wheat")
ax3.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=8) #move legend outside to make room
#display numbers in full form
ax3.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax3.tick_params(axis='y', labelsize=6) #format y axis labels

plt.tight_layout(pad=1.0)

###

#NOVEMBER DATA
soy_countries_n, sn2024 = get_commodity_nov(df_nov, "Soybeans", 10)
corn_countries_n, cn2024 = get_commodity_nov(df_nov, "Corn", 10)
wheat_countries_n, wn2024 = get_commodity_nov(df_nov, "Wheat, unmilled", 11)

#set up layout (november window)
fig2 = plt.figure(figsize=(10, 6))
fig2.suptitle("Exports for Soybeans, Corn, and Wheat (Jan - Nov 2024)", fontsize=14)

ax4 = plt.subplot(2, 2, 1) #soybeans graph
ax5 = plt.subplot(2, 2, 2) #corn graph
ax6 = plt.subplot(2, 1, 2) #wheat graph

#Soybeans - Pie Chart
valid = sn2024 > 0
wedges, _ = ax4.pie(
    sn2024[valid],
    startangle=250
) #create wedges
ax4.set_title("Soybeans")
ax4.legend(
    wedges,
    soy_countries_n[valid],
    title="Countries",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=7
)#create legend from wedges

#Corn - Horizontal Bar Chart
corn_countries_n = corn_countries_n[::-1]
cn2024 = cn2024[::-1]

y = np.arange(len(corn_countries_n))
ax5.invert_yaxis() #format so its the same as given graph
ax5.barh(y, cn2024, label="2024")
ax5.set_yticks(y)
ax5.set_yticklabels(corn_countries_n, fontsize=7)
#display numbers in full form
ax5.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax5.tick_params(axis='x', labelsize=6) #format x axis labels
ax5.set_title("Corn")

#Wheat - Shaded Line Chart
x = np.arange(len(wheat_countries_n))
ax6.plot(x, wn2024, marker="o", color='blue', label="2024")
wn2024_float = wn2024.astype(float) #convert to float type so fill function works
ax6.fill_between(x, wn2024_float, 0, color='blue', alpha=0.15)
ax6.set_xticks(x)
ax6.set_xticklabels(wheat_countries_n, rotation=45, ha="right", fontsize=7)
#display numbers in full form
ax6.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax6.tick_params(axis='y', labelsize=6) #format y axis labels
ax6.set_title("Wheat")

plt.tight_layout(pad=1.0)


plt.show() #display graph windows
