# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

#Task 1
total = df.shape[0]
p_a = len(df[df['fico'] > 700]) / total

p_b = len(df[df['purpose'] == 'debt_consolidation']) / total

p_a_b = len(df[(df['fico'] > 700) & (df['purpose'] == 'debt_consolidation')]) / total
p_a_b = p_a_b / p_b

result = p_a_b == p_a
print(result)

#Task 2
prob_lp = len(df[df['paid.back.loan'] == 'Yes']) /total

prob_cs = len(df[df['credit.policy'] == 'Yes']) /total

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(df[(df['paid.back.loan'] == 'Yes') & (df['credit.policy'] == 'Yes')]) / total
bayes = prob_pd_cs / prob_cs
print(bayes)

#Task 3
df['purpose'].value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution of Purpose")
plt.ylabel("Probability")
plt.xlabel("Number of Purpose")
plt.show()

df1 = df[df['paid.back.loan'] == 'No']

df1['purpose'].value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution of Purpose")
plt.ylabel("Probability")
plt.xlabel("Number of Purpose")
plt.show()

#Task 4
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].hist(normed = True, bins=50)
plt.axvline(x=inst_median, color='r')
plt.axvline(x=inst_mean, color='g')
plt.show()

df['log.annual.inc'].hist(normed = True, bins=50)
plt.show()



