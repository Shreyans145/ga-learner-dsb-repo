# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter = ",", skip_header=1)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((new_record,data))
#Code starts here



# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.sum()/len(age)
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

race_list = [len_0, len_1,len_2, len_3, len_4]
minority_race = race_list.index(min(race_list))
print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
#race_4 = census[census[:,2]==4]
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
import numpy
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high = (high.sum(axis=0)[7])/len(high)
print(avg_pay_high)
avg_pay_low = (low.sum(axis=0)[7])/len(low)
print(avg_pay_low)
numpy.equal(avg_pay_high,avg_pay_low)


