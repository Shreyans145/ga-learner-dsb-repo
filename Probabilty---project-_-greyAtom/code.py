# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

# probability of  fico score greater than 700

p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)


# probability of purpose == debt_consolidation
p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

# Create new dataframe for condition ['purpose']== 'debt_consolidation' 
df1 = df[df['purpose']== 'debt_consolidation']

# Calculate the P(A|B)
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes' ].shape[0]/df.shape[0]
print(prob_lp)

prob_cs = df[df['credit.policy'] == 'Yes' ].shape[0]/df.shape[0]
print(prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']
print(new_df)

prob_pd_cs= new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)

bayes = (prob_pd_cs*prob_lp)/(prob_cs)
print(bayes)
# code ends here


# --------------
# code starts here
df.purpose.value_counts(normalize=True).plot(kind='bar')

df1 = df[df['paid.back.loan']== 'No']

df1.purpose.value_counts(normalize=True).plot(kind='bar')

# code ends here


# --------------
# code starts here
inst_median = df.installment.median()
print(inst_median)

inst_mean = df.installment.mean()
print(inst_mean)

df['installment'].hist(normed = True, bins=50)
df['log.annual.inc'].hist(normed = True, bins=50)

# code ends here


