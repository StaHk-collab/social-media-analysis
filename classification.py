import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as metrics
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import roc_auc_score

import warnings
warnings.filterwarnings('ignore') # setting ignore as a parameter


# Data Visualization

df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')

# print(df1.info())
# print(df2.info())

# #Tweets

plt.title("#Tweets (On data1)")
plt.scatter(df1['#Tweets'], df1['H(u, I)'], color = "red", label = "Interaction Diversity(Random)", alpha = 0.8)
plt.scatter(df1['#Tweets'], df1['Engagement (Random)'], color = "blue", label = "Engagement(Random)", alpha = 0.8)
plt.scatter(df1['#Tweets'], df1['Activity (Random)'], color = "green", label = "Activity(Random)", alpha = 0.3)
plt.legend()
plt.show()

plt.title("#Tweets (On data2)")
plt.scatter(df2['#Tweets'], df2['H(u, I)'], color = "red", label = "Interaction Diversity(ED)", alpha = 0.8)
plt.scatter(df2['#Tweets'], df2['Engagement (ED)'], color = "blue", label = "Engagement(ED)", alpha = 0.8)
plt.scatter(df2['#Tweets'], df2['Activity (ED)'], color = "green", label = "Activity(ED)", alpha = 0.3)
plt.legend()
plt.show()

# Followees

plt.title("Followees (On data1)")
plt.scatter(df1['Followees'], df1['H(u, I)'], color = "red", label = "Interaction Diversity(Random)", alpha = 0.8)
plt.scatter(df1['Followees'], df1['Engagement (Random)'], color = "blue", label = "Engagement(Random)", alpha = 0.8)
plt.scatter(df1['Followees'], df1['Activity (Random)'], color = "green", label = "Activity(Random)", alpha = 0.3)
plt.legend()
plt.show()

plt.title("Followees (On data2)")
plt.scatter(df2['Followees'], df2['H(u, I)'], color = "red", label = "Interaction Diversity(ED)", alpha = 0.8)
plt.scatter(df2['Followees'], df2['Engagement (ED)'], color = "blue", label = "Engagement(ED)", alpha = 0.8)
plt.scatter(df2['Followees'], df2['Activity (ED)'], color = "green", label = "Activity(ED)", alpha = 0.3)
plt.legend()
plt.show()

# Followers

plt.title("Followers (On data1)")
plt.scatter(df1['Followers'], df1['H(u, I)'], color = "red", label = "Interaction Diversity(Random)", alpha = 0.8)
plt.scatter(df1['Followers'], df1['Engagement (Random)'], color = "blue", label = "Engagement(Random)", alpha = 0.8)
plt.scatter(df1['Followers'], df1['Activity (Random)'], color = "green", label = "Activity(Random)", alpha = 0.3)
plt.legend()
plt.show()

plt.title("Followers (On data2)")
plt.scatter(df2['Followers'], df2['H(u, I)'], color = "red", label = "Interaction Diversity(ED)", alpha = 0.8)
plt.scatter(df2['Followers'], df2['Engagement (ED)'], color = "blue", label = "Engagement(ED)", alpha = 0.8)
plt.scatter(df2['Followers'], df2['Activity (ED)'], color = "green", label = "Activity(ED)", alpha = 0.3)
plt.legend()
plt.show()


# Classification

# Form an array of ED and Random separately with the all the 3 attributes Engagement, Diversity and 
# Interaction Activity. Make one test and one predicted and then follow the bookmarked page

# Random (Test)
d1 = pd.DataFrame()
d1['#Tweets'] = df1['#Tweets']
d1['#Re-Tweets'] = df1['#Re-Tweets']
d1['Followers'] = df1['Followers']
d1['Followees'] = df1['Followees']
d1['Engagement (Random)'] = df1['Engagement (Random)']
d1['Activity (Random)'] = df1['Activity (Random)']
d1['Interaction Diversity (Random)'] = df1['H(u, I)']
d1['Ed-ed'] = df2['Ed-ed'].astype(int)
d1.to_csv('d1.csv')

# ED (Pred)
d2 = pd.DataFrame()
d2['S.No.'] = df2['Unnamed: 0']
d2['#Tweets'] = df2['#Tweets']
d2['#Re-Tweets'] = df2['#Re-Tweets']
d2['Followers'] = df2['Followers']
d2['Followees'] = df2['Followees']
d2['Engagement (ED)'] = df2['Engagement (ED)']
d2['Activity (ED)'] = df2['Activity (ED)']
d2['Interaction Diversity (ED)'] = df2['H(u, I)']
d2.to_csv('d2.csv')

# Classification

# Assign values to the X and y variables:
X = d1.iloc[:, :7].values
y = d1.iloc[:, 7].values

print(X.shape, y.shape)

# Split dataset into random train and test subsets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# # Standardize features by removing mean and scaling to unit variance:
# scaler = StandardScaler()
# scaler.fit(X_train)

# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# Use the KNN classifier to fit data:
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

# Predict y data with classifier: 
y_predict = classifier.predict(X_test)

# Print results: 
# print(confusion_matrix(y_test, y_predict))
# print(classification_report(y_test, y_predict))
print('f1 score :', metrics.f1_score(y_test, y_predict, average='weighted', labels=np.unique(y_predict)))
print('accuracy_score :', metrics.accuracy_score(y_test, y_predict, normalize=True, sample_weight=None))

# clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# print('clf score :', clf.score(X_test, y_test))

# clf = svm.SVC(kernel='linear', C=1, random_state=42)
# scores = cross_val_score(clf, X, y, cv=5)
# print('CV score :', scores)

# print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))

# ROC
y_scores = classifier.predict_proba(X_test)
fpr, tpr, threshold = roc_curve(y_test, y_scores[:, 1])
roc_auc = auc(fpr, tpr)

plt.title('ED-Random Classification')
plt.plot(fpr, tpr, 'b')
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Curve')
plt.show()

