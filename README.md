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
-   H(u, I) = −Summation(v∈Tu) p(Iv) log p(Iv), where I ∈ {Hashtag, Re-tweet, Mention, Reply}, and p(Iv) = #Iv / (Summation(j∈Tu) #Ij). #Iv is the number of interactions I with target v, e.g., using hashtag v or re-tweeting user v. Larger entropy values indicate a higher diversity of interests that a user has.

After that they are stored in a csv file.

## Data Visualization<a name="visualize"></a>

<p align="left">  <p align="right">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_1.png">  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_2.png">
</p>  </p>

<p align="left"> <p align="right">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_3.png">  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_4.png">
</p> </p>

## Classification<a name="classify"></a>

K Nearest Neighbour (KNN) and linear Support Vector Machine (SVM) classifiers are used to further verify the reliability of data sampling method. The best performing classifier is found to be linear SVM with the default settings in Scikit-learn 1.1.1 package, with an accuracy score of 99.62962962962963%

## ROC Curve<a name="curve"></a>

<p align="center">
  <img width="489" height="355" src="https://github.com/StaHk-collab/social-media-analysis/blob/main/Figures/Figure_5.png">
</p>

## Resources<a name="resources"></a>

- https://dl.acm.org/doi/pdf/10.1145/3018661.3018706
- https://docs.tweepy.org/en/stable/
- https://scikit-learn.org/stable/supervised_learning.html#supervised-learning
