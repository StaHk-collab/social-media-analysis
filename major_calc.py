import pandas as pd
import numpy as np
from datetime import datetime

# Statistics of bio-information in ED-ed users

data1 = pd.read_csv('ED.csv')

data2 = pd.read_csv('final.csv')
data2 = data2.drop("Unnamed: 0", axis='columns')
data2 = data2.drop("Unnamed: 0.1", axis='columns')
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

# Followers (On data2)
mean_2 = data2['Followers'].mean()
var_2 = data2['Followers'].var()
std_2 = data2['Followers'].std()
print('Followers (On data2) :')
print('Mean :', mean_2, ', Var :', var_2, ', Std :', std_2)

# Followees (On data1)
mean_3 = data1['Followees'].mean()
var_3 = data1['Followees'].var()
std_3 = data1['Followees'].std()
print('Followees (On data1) :')
print('Mean :', mean_3, ', Var :', var_3, ', Std :', std_3)

# Followees (On data2)
mean_4 = data2['Followees'].mean()
var_4 = data2['Followees'].var()
std_4 = data2['Followees'].std()
print('Followees (On data2) :')
print('Mean :', mean_4, ', Var :', var_4, ', Std :', std_4)

# #Tweets (On data1)
mean_5 = data1['#Tweets'].mean()
var_5 = data1['#Tweets'].var()
std_5 = data1['#Tweets'].std()
print('#Tweets (On data1) :')
print('Mean :', mean_5, ', Var :', var_5, ', Std :', std_5)

# #Tweets (On data2)
mean_6 = data2['#Tweets'].mean()
var_6 = data2['#Tweets'].var()
std_6 = data2['#Tweets'].std()
print('#Tweets (On data2) :')
print('Mean :', mean_6, ', Var :', var_6, ', Std :', std_6)

# #Re-Tweets (On data1)
mean_7 = data1['#Re-Tweets'].mean()
var_7 = data1['#Re-Tweets'].var()
std_7 = data1['#Re-Tweets'].std()
print('#Re-Tweets (On data1) :')
print('Mean :', mean_7, ', Var :', var_7, ', Std :', std_7)

# #Re-Tweets (On data2)
mean_8 = data2['#Re-Tweets'].mean()
var_8 = data2['#Re-Tweets'].var()
std_8 = data2['#Re-Tweets'].std()
print('#Re-Tweets (On data2) :')
print('Mean :', mean_8, ', Var :', var_8, ', Std :', std_8)

# Hashtags (On data1)
mean_9 = data1['Hashtags'].mean()
var_9 = data1['Hashtags'].var()
std_9 = data1['Hashtags'].std()
print('Hashtags (On data1) :')
print('Mean :', mean_9, ', Var :', var_9, ', Std :', std_9)

# Hashtags (On data2)
mean_10 = data2['Hashtags'].mean()
var_10 = data2['Hashtags'].var()
std_10 = data2['Hashtags'].std()
print('Hashtags (On data2) :')
print('Mean :', mean_10, ', Var :', var_10, ', Std :', std_10)


# 1. Social Status

# Engagement(u, s) = log (1 + #su), where s ∈ {Followees, Tweets, Followers}, and #su denotes the count of s that u has.

## Random (On data1)
data1['Engagement (Random)'] = np.log(1 + data1['Followees'] + data1['Followers'] + data1['#Tweets'])
# data1.to_csv('data1.csv')
mean1 = data1['Engagement (Random)'].mean()
var1 = data1['Engagement (Random)'].var()
std1 = data1['Engagement (Random)'].std()
print('Engagement (On data1) :')
# print('Mean :', mean1, ', Var :', var1, ', Std :', std1)

# Standardization: (x - mean)/std
data1['Engagement (Random)'] = (data1['Engagement (Random)'] - mean1)/std1

## ED (On data2)
data2['Engagement (ED)'] = np.log(1 + data2['Followees'] + data2['Followers'] + data2['#Tweets'])
# data2.to_csv('data2.csv')
mean2 = data2['Engagement (ED)'].mean()
var2 = data2['Engagement (ED)'].var()
std2 = data2['Engagement (ED)'].std()
print('Engagement (On data2) :')
print('Mean :', mean2, ', Var :', var2, ', Std :', std2)

# Standardization: (x - mean)/std
data2['Engagement (ED)'] = (data2['Engagement (ED)'] - mean2)/std2

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
    data1['Activity (Random)'] = np.log(1 + (data1['Followees'] + data1['Followers'] + data1['#Tweets'])/(days))

# data1.to_csv('data1.csv')
mean3 = data1['Activity (Random)'].mean()
var3 = data1['Activity (Random)'].var()
std3 = data1['Activity (Random)'].std()
print('Activity (On data1) :')
print('Mean :', mean3, ', Var :', var3, ', Std :', std3)

# Standardization: (x - mean)/std
data1['Activity (Random)'] = (data1['Activity (Random)'] - mean3)/std3

## ED (On data2)
c = 0
maxi = 0
for i in data2:
    if maxi != 2:
        str_1 = str(data2['Date of Joining'][c])
        str_2 = str(data2['Date of Last Post'][c])
        c += 1
        # str_1
        count = 0
        year1 = ""
        month1 = ""
        day1 = ""
        for i in str_1:
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
        # str_2
        count = 0
        year2 = ""
        month2 = ""
        day2 = ""
        for i in str_2:
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
        maxi += 1
    else:
        break
    days = (int(year2) - int(year1))*365 + (int(month2) - int(month1))*30 + (int(day2) - int(day1))
    data2['Activity (ED)'] = np.log(1 + (data2['Followees'] + data2['Followers'] + data2['#Tweets'])/(days))

# data2.to_csv('data2.csv')
mean4 = data2['Activity (ED)'].mean()
var4 = data2['Activity (ED)'].var()
std4 = data2['Activity (ED)'].std()
print('Activity (On data2) :')
print('Mean :', mean4, ', Var :', var4, ', Std :', std4)

# Standardization: (x - mean)/std
data2['Activity (ED)'] = (data2['Activity (ED)'] - mean4)/std4

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

# Standardization: (x - mean)/std
data1['H(u, I)'] = (data1['H(u, I)'] - mean5)/std5

data1.to_csv('data1.csv') #

## ED (On data2)
data2['p(Iv)'] = (data2['#Re-Tweets'] + data2['Hashtags'])/(data2['#Re-Tweets'].sum() + data2['Hashtags'].sum())
data2['H(u, I)'] = data2['p(Iv)'] * np.log(1 + data2['p(Iv)'])

mean6 = data2['H(u, I)'].mean()
var6 = data2['H(u, I)'].var()
std6 = data2['H(u, I)'].std()
print('H(u, I) (On data2) :')
print('Mean :', mean6, ', Var :', var6, ', Std :', std6)

# Standardization: (x - mean)/std
data2['H(u, I)'] = (data2['H(u, I)'] - mean6)/std6

data2.to_csv('data2.csv') #