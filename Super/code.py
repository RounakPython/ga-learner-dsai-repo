# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-', 'Agender', inplace=True)
gender_count = data['Gender'].value_counts()

plt.bar(gender_count.index, gender_count)
plt.show()

alignment = data['Alignment'].value_counts()
plt.figure(figsize=(6,6))

plt.pie(alignment, labels=alignment.index, explode=(0.05,0.05,0.05), autopct='%1.1f %%')

plt.title('Character Alignment')

sc_df = data[['Strength', 'Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]

sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance/(sc_strength*sc_combat)
print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)

ic_df = data[['Intelligence', 'Combat']].copy()

ic_covariance = ic_df.cov().iloc[0,1]

ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)

total_high = data['Total'].quantile(q=0.99)

super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)






