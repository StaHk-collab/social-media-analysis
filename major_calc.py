import pandas as pd
import numpy as np
from datetime import datetime

# Statistics of bio-information in ED-ed users

data1 = pd.read_csv('dataset.csv')

# data2 = pd.read_csv('final.csv')
# data2 = data2.drop("Unnamed: 0", axis='columns')
# data2 = data2.drop("Unnamed: 0.1", axis='columns')
# data2.to_csv('data2.csv')

data_2 = data1[data1['Tweet'].str.contains('CW', case=False)]
data_3 = data1[data1['Tweet'].str.contains('LW', case=False)]
data_4 = data1[data1['Tweet'].str.contains('HW', case=False)]
data_5 = data1[data1['Tweet'].str.contains('GW', case=False)]
data_6 = data1[data1['Tweet'].str.contains('UGW', case=False)]

# % Users

print('CW', data_2.shape[0])
print('LW', data_3.shape[0])
print('HW', data_4.shape[0])
print('GW', data_5.shape[0])
print('UGW', data_6.shape[0])

# %Users

print('%CW', (data_2.shape[0]/data1.shape[0])*100)
print('%LW', (data_3.shape[0]/data1.shape[0])*100)
print('%HW', (data_4.shape[0]/data1.shape[0])*100)
print('%GW', (data_5.shape[0]/data1.shape[0])*100)
print('%UGW', (data_6.shape[0]/data1.shape[0])*100)

# Mean, Variance and Standard Deviaton of Followers, Followees, #Tweets, #Re-Tweets, Hashtags

# Followers (On data1)
mean_1 = data1['Followers'].mean()
var_1 = data1['Followers'].var()
std_1 = data1['Followers'].std()
print('Followers (On data1) :')
print('Mean :', mean_1, ', Var :', var_1, ', Std :', std_1)

# Followees (On data1)
mean_3 = data1['Followees'].mean()
var_3 = data1['Followees'].var()
std_3 = data1['Followees'].std()
print('Followees (On data1) :')
print('Mean :', mean_3, ', Var :', var_3, ', Std :', std_3)

# #Tweets (On data1)
mean_5 = data1['#Tweets'].mean()
var_5 = data1['#Tweets'].var()
std_5 = data1['#Tweets'].std()
print('#Tweets (On data1) :')
print('Mean :', mean_5, ', Var :', var_5, ', Std :', std_5)

# #Re-Tweets (On data1)
mean_7 = data1['#Re-Tweets'].mean()
var_7 = data1['#Re-Tweets'].var()
std_7 = data1['#Re-Tweets'].std()
print('#Re-Tweets (On data1) :')
print('Mean :', mean_7, ', Var :', var_7, ', Std :', std_7)

# Hashtags (On data1)
mean_9 = data1['Hashtags'].mean()
var_9 = data1['Hashtags'].var()
std_9 = data1['Hashtags'].std()
print('Hashtags (On data1) :')
print('Mean :', mean_9, ', Var :', var_9, ', Std :', std_9)

# 1. Social Status

# Engagement(u, s) = log (1 + #su), where s ∈ {Followees, Tweets, Followers}, and #su denotes the count of s that u has.

## Random (On data1)
data1['Engagement'] = np.log(1 + data1['Followees'] + data1['Followers'] + data1['#Tweets'])
# data1.to_csv('data1.csv')
mean1 = data1['Engagement'].mean()
var1 = data1['Engagement'].var()
std1 = data1['Engagement'].std()
print('Engagement (On data1) :')
print('Mean :', mean1, ', Var :', var1, ', Std :', std1)

# Activity(u, s) = log(1 + #su/tu), where tu denotes the number of days from the date of u's joining Twitter to the date of u’s last post

## Random (On data1)
c = 0
for i in data1:
    str1 = str(data1['Date of Joining'][c])
    str2 = str(data1['Date of Last Post'][c])
    c += 1
    # str1
    count = 0
    year1 = ""
    month1 = ""
    day1 = ""
    for i in str1:
        if count == 4:
            break
        if i != '-' and count == 0:
            year1 += i
        elif i != '-' and count == 1:
            month1 += i
        elif i != '-' and (count == 2 or count == 3):
            day1 += i
            count += 1
            continue
        else:
            count += 1
    # str2
    count = 0
    year2 = ""
    month2 = ""
    day2 = ""
    for i in str2:
        if count == 4:
            break
        if i != '-' and count == 0:
            year2 += i
        elif i != '-' and count == 1:
            month2 += i
        elif i != '-' and (count == 2 or count == 3):
            day2 += i
            count += 1
            continue
        else:
            count += 1
    days = (int(year2) - int(year1))*365 + (int(month2) - int(month1))*30 + (int(day2) - int(day1))
    data1['Activity'] = np.log(1 + (data1['Followees'] + data1['Followers'] + data1['#Tweets'])/(days))

# data1.to_csv('data1.csv')
mean3 = data1['Activity'].mean()
var3 = data1['Activity'].var()
std3 = data1['Activity'].std()
print('Activity (On data1) :')
print('Mean :', mean3, ', Var :', var3, ', Std :', std3)

# 2. Behavioral Patterns (Interaction Diversity)

# The interest diversity of u in terms of a type of interactions I is computed by calculating the entropy of such interactions with different targets v ∈ Tu:
# Given a user u, we track the sequence of targets of interest to u (e.g., hashtags u used or other users u re-tweeted in the past), denoted as Tu.
# H(u, I) = −Summation(v∈Tu) p(Iv) log p(Iv), where I ∈ {Hashtag, Re-tweet, Mention, Reply}, and
# p(Iv) = #Iv / (Summation(j∈Tu) #Ij). #Iv is the number of interactions I with target v, e.g., using hashtag v or re-tweeting user v.
# Larger entropy values indicate a higher diversity of interests that a user has.

## Random (On data1)
data1['p(Iv)'] = (data1['#Re-Tweets'] + data1['Hashtags'])/(data1['#Re-Tweets'].sum() + data1['Hashtags'].sum())
data1['H(u, I)'] = data1['p(Iv)'] * np.log(1 + data1['p(Iv)'])

data1 = data1.drop("Unnamed: 0", axis='columns')

mean5 = data1['H(u, I)'].mean()
var5 = data1['H(u, I)'].var()
std5 = data1['H(u, I)'].std()
print('H(u, I) (On data1) :')
print('Mean :', mean5, ', Var :', var5, ', Std :', std5)

data1['ED-ed'] = data1['Ed-ed'].astype(int)

print('The total no. of Users (Random) :', 900)
print('Total no of Random Tweets :', data1['#Tweets'].sum())
print('No.of Tweets per User (Random) :', (data1['#Tweets'].sum())/900)

# ED-ed user tweets
tweets = 0
for i in range(942):
    if data1['ED-ed'][i] == 1:
        tweets = tweets + data1['#Tweets'][i]

print('The total no. of Users (ED) :', data1['ED-ed'].value_counts()[1])
print('Total no. of Tweets (ED-ed) :', tweets)
print('No. of Tweets per User (ED-ed) :', tweets/(data1['ED-ed'].value_counts()[1]))

data1.to_csv('data1.csv') #
