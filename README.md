# Social Media Analysis Using Twitter Data

1. [Project Motivation](#motivation)
2. [Proposed Model](#proposedmodel)
3. [Dataset Construction](#dataset)
4. [Data Visualization](#visualize)
5. [Classification](#classify)
6. [ROC Curve](#curve)
7. [Recources](#resources)

## Project Motivation <a name="motivation"></a>

Recent studies reveal that user-generated content on social media provides useful information in understanding these disorders. Most previous studies focus on studying communities of people who discuss eating disorders on social media, while few studies have explored community structures and interactions among individuals who suffer from this disease over social media.

## Proposed Model <a name="proposedmodel"></a>

First snowball sampling method is used to automatically gather individuals who self-identify as eating disordered in their profile descriptions, as well as their social network connections with one another on Twitter. Then, we verify the effectiveness of the sampling method by quantifying differences between the sampled eating disordered users and random data collected for non-disordered users in social status, behavioral patterns and psychometric properties. Then building predictive models to classify eating disordered and non-disordered users.

##  Dataset Construction <a name="dataset"></a>

The data is collected using Twitter API, Tweepy a library of Python is used for the same. Around 1000 tweets are collected for performing the analysis. The features that were collected directly using Twitter API are :
-    Tweets which have the keywords for ED Diagnosis and then they are further pre-processed with the keywords containing the bio-information keywords
-    No. of Tweets
-    No. of Re-Tweets
-    No. of Hashtags
-    Date of Joining Twitter
-    Date of Last Post
-    No. of Replies

After that the values of each feature is standardized by subtracting the corresponding mean and dividing by the corresponding standard deviation.

Next the following properties were calculated :
- #### Social Status
-   Engagement(u, s) = log (1 + #su), where s ∈ {Followees, Tweets, Followers}, and #su denotes the count of s that user(u) has.
-   Activity(u, s) = log(1 + #su/tu), where tu denotes the number of days from the date of u's joining Twitter to the date of u’s last post

- #### Behavioral Patterns (Interaction Diversity)
-   The interest diversity of u in terms of a type of interactions I is computed by calculating the entropy of such interactions with different targets v ∈ Tu: Given a user u, we track the sequence of targets of interest to u (e.g., hashtags u used or other users u re-tweeted in the past), denoted as Tu.
    <p align="left"> <img width="280" height="80" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_7.png"> </p>
where I ∈ {Hashtag, Re-tweet, Mention, Reply} and #Iv is the number of interactions I with target v. Larger entropy values indicate a higher diversity of interests that a user has.

After that they are stored in a *CSV* file.

### Keywords of ED-ed diagnoses and bio-information used for filtering ED-ed users :

Category | Keywords
--- | ---
ED diagnosis | eating disorder, eatingdisorder, anorexia, anorexic, anorexia nervosa, bulimia, bulimic, bulemia, bulimia nervosa, ednos, edprob, proana, promia, anamia, askanamia, purge, binge, thinspo, bonespo, legspo
Bio-information | BMI (Body Mass Index), CW (Current Weight), UGW (Ultimate Goal Weight), GW (Goal Weight), HW (Highest Weight), LW (Lowest Weight), lbs, kg

### Mean, Standard Deviation of the features :

Features | Mean | Standard Deviation
--- | --- | ---
Followers | 5976.542462845011 | 118892.81833646235
Followees | 856.3885350318471 | 2347.434503889102
#Tweets | 24214.196390658173 | 88794.20052256041
#Re-Tweets | 26.633757961783438 | 79.05593767797122
Hashtags | 0.06687898089171974 | 0.4973752832357883
Engagement | 8.055438475263188 | 2.1522315331748194
Activity | 3.751510672064837 | 1.977088733976534
H(u, I) (Interaction Diversity) | 1.0796611544093487e-05 | 0.00015037222305051219

## Data Visualization<a name="visualize"></a>

### Statistics of no. of users, no. of tweets, and average no. of tweets per user :

Dataset | User | Tweets | Tweets per User
---- | ---- | ---- | ----
Random | 942 | 22809773 | 24214.196
ED | 50 | 561709 | 11234.18

<p align="center">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_1.png">
</p>

<p align="center">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_2.png">
</p>

<p align="center">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_3.png">
</p>

## Classification<a name="classify"></a>

K Nearest Neighbour (KNN) and linear Support Vector Machine (SVM) classifiers are used to further verify the reliability of data sampling methods.

### Performance of Predicting the classes of ED-Random Users :

Measure | ED-Random
--- | ---
Accuracy | 0.951
Precision | 0.95
Recall | 1.00
F1 | 0.974



## ROC Curve<a name="curve"></a>

#### AUC : 64.923%

<p align="center">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_4.png">
</p>

#### Logistic Regression (AUC : 64.365%)

<p align="center">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_6.png">
</p>

## Resources<a name="resources"></a>

- https://dl.acm.org/doi/pdf/10.1145/3018661.3018706
- https://docs.tweepy.org/en/stable/
- https://scikit-learn.org/stable/supervised_learning.html#supervised-learning
