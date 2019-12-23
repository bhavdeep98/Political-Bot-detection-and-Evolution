
 PDF To Markdown Converter
Debug View
Result View
# Evolution of Bots

### Fall 2019 CSE-472 Social Media Mining Project II

## Bhavdeep S. Sachdeva^1 (1217205756), Sai Pramod V.^1 (1217195369), Tahora H. Nazer^1 ∗

(^1) Arizona State University
```
∗PhD. Guide
```
## {bssachde, svallab6, tahora.nazer}@asu.edu

## 1 Introduction

In 2011, a seven months long study by [LEC11] identified four types of bot accounts lurking around us on Twitter:Du-
plicate Spammers,Duplicate @Spammer,Malicious Promoters, andFriend Infiltrators. Since then bots have deeply
embedded themselves into our social media networks. Despite all their nefarious uses, there are examples of bots pro-
viding valuable services to social media users [Møn+17]. Some of these ”good” bots have mitigated the effect of the
so called nefarious bots. Different typologies of these bots have been shown in [Sti+17], and have been summarized by
Matthew Davis, from the Data Mining and Machine Learning (DMML) lab at Arizona State University(ASU), in Figure 1.

```
Figure 1: Example Typology of Bots
```
One example of how bots have been identified according to their intents can be seen in a study by [Yan+19], which
classifies bots into the following major categories: Simple bots(Obvious to human users, post many tweets to make con-
tent visible),Sophisticated bots(Interact with human users by exploiting retweets, hashtags, and mentions),Fake Follow-
ers(Increase the popularity of and lend credibility to some other users on the network), andBotnets(Use coordination
to interact with each other and/or human users on the network). Twitter bots in general have had a significant impact in
the 2016 general elections and 2018 midterm elections. In a study conducted by [BF16], it was found that there are about
400,000 bots that were engaged in 2016 online discussions about Presidential election, responsible for roughly 3.8 mil-
lion tweets, about one fifth of the entire conversation. The main intent of the creators of these malicious bot accounts is,
rather simply, to behave such that the accounts are not identified as bots and continue fooling bot detection technologies
while still fulfilling their malicious agenda on Twitter. This is an eternal hide-and-seek between the bots and the bot de-
tection methodologies. In our research we aim at identifying how these bots have evolve over time and managed to evade
these detection techniques.
```
## 2 Terminology

### 2.1 Social Bots

```
A social bot, also known as Sybil account, allows the human user to programmatically produce content on social media.
These accounts interact with other bots as well as humans. If the bot once created does not have any human intervention af-
terwards it is regarded as afully automated bot. Alternatively, if the bot has certain human control involved it is regarded as asemi-automated bot[18].
```
### 2.2 Botnet API aka Bot or Not [Dav+16]

```
Botnet API is a web service that was made public in May 2014. The service provides the bot-likelihood of a user us-
ing the in-house classifier. TheBotOrNotclassifier generates more than 1,000 features using the available meta data from
the Twitter API^1. These features consists of following 6 main classes:networkinformation diffusion patterns,usertwitter
meta data related to the account,friendsdescriptive statistics related to accounts social contacts,temporal featuressuch
as the date of creation, inter tweet time distribution,content features based on linguistics cues computer through natural
language processing, andsentimentbuilt using general purpose and Twitter specific sentiment analysis.

## 3 Data Summary

```
To identify how bots evolve over time, we must analyse
temporal data of bots, collected over different periods of
```
(^1) dev.twitter.com/rest/public


time. In our literature survey, we found two major techniques
used to gather data for the classification and analysis of
bots. The most common method involved identifying a
certain set of hashtags on Twitter, and scraping data of bots
tweeting/retweeting/liking content related to those hashtags.
Many researchers such as [HKW16], [Su ́a+16], and [HK16]
have used this technique to obtain bot data from Twitter.
Uniquely, [LEC11] collected bot-related data from Twitter
using theHoneyPotmethod. HoneyPot Twitter accounts are
intentionally designed to avoid interfering with the activities
of legitimate users and lure bot accounts with their activity.
They only send @replies to each other, and only follow
other honeypots. They researchers claim to have certain
advantages of using this technique over others, namely ”(1)
automatically collecting evidence of content polluters; (2)
no interference or intrusion on the activities of legitimate
users in the system; and (3) robustness of ongoing polluter
identification and filtering, since new evidence of polluter
behavior and strategy can be easily incorporated into con-
tent polluter models.” [LEC11]. The data collected using the
honeypots was implicitly labeled as bots.

For our analysis we used theCaverlee-2011data-set^2
which consisted of bot data collected using the HoneyPot
method. We considered many other bots data sets available
online as well, but a huge majority of the bot accounts
in those data-sets were already taken down by Twitter.
However, the Caverlee 2011 data-set, which is summarized
in Table 1, was collected in 2011 but still contains about
14,321 bots that are active on Twitter in 2019. These active
bots were re-scrapped by Matthew Davis from the Data
Mining and Machine Learning (DMML) lab at Arizona State
University (ASU), and this formed ourCaverlee-2019data
set. Thus, our analysis consisted of studying and comparing
very similar bots, and how they have evolved over time.
Since the Caverlee-2019 data set consists of bots from 2011
that are still active, studying these two sets of bots gave us
a good understanding of how bots have changed over time
and also helped identify possible reasons for their survival by
evading bot-detection technologies.

```
Property Caverlee 2011
Tweets 2,353,
Retweets 63,
Accounts 20,
Active 14,
Suspended 4,
Deleted 1,
Labeling Approach Honeypot
```
```
Table 1: Summary Caverlee 2011
```
(^2) https://botometer.iuni.iu.edu/bot-repository/datasets.html

## 4 Feature Selection

```
The Caverlee 2011 data-set contains feature values of
bots which are divided into three major categories,profile
information, followers information and tweets. The
profile information consisted of the following attributes,
“UserID, CreatedAt, CollectedAt, NumerOfFollowings,
NumberOfFollowers, NumberOfTweets, LengthOfScreen-
Name, LengthOfDescriptionInUserProfile”. Apart from
these features, another important feature for our analysis
could be the difference between the number of followings
and the number of followers of a bot, or a similar ratio of the
two values. We chose to move ahead with the difference and
engineered a new feature calledfoll-difference, which was
defined as the difference between the NumberOfFollowings
and NumberOfFollowers for each of the data points.
The Caverlee-2019 data consisted of JSON objects, which
had many attributes. We extracted the relevant attributes,
which included “UserID, followers-count, friends-count,
statuses-count, screen-name, and description”. We con-
structed a new feature called length-screen-name by
calculating the length of the screen-name attribute for each of
the data points. Similarly, a new featurelength-description
was obtained by calculating the length of the Description fea-
ture for each bot. The featuresscreen-nameanddescription
were then dropped and replaced by thelength-screen-name
andlength-descriptionrespectively, since the absolute values
of the name and description do not matter for our analysis.
```
## 5 Model Description

```
The primary method of clustering used for the formation
of categories of bots in both the Caverlee-2011 and the
Caverlee-2019 data sets wasK-Means clustering. The op-
timal number of clusters,k, was chosen using theElbow
Methodas well as thesilhouette scores. The Elbow method
consisted of a plot ofkvsinertia(the sum of squared dis-
tances of samples to their closest cluster center). After identi-
fying a range of possible values for k with low inertia, the best
value was picked as the value that maximizes the silhouette
score. The optimal number of clusters in the Caverlee-
data set chosen this way turned out to be 5, while in the case
of the Caverlee-2019 data set, it turned out to be 7. Also,
since our analysis involves comparing the two data sets, the
optimal k was chosen such that the inertia values were simi-
lar too. Clustering with k = 5 on the Caverlee-2011 data set
produced an inertia value of 1.322, while clustering with k =
7 on the Caverlee-2019 data set produced an inertia value of
1.360. Thus, these values were chosen as the optimal number
of clusters in each case.
The cluster centers were obtained as a result of the clustering,
and the euclidean distances matrices computed for the cen-
ters in each of the cases. Again, the norms of these matrices
turned out to be similar, 2.462 and 2.547 respectively, thus in-
dicating that our choice of optimal number of clusters is right.
```

Cluster No.of Bots following-count follower-count statuses-count len-nameandlen-descr foll-diff

```
1 12203 5 5 5 - +(2)
2 554 1 2 2 - -(1)
3 9343 4 4 4 - +(1)
4 121 3 3 1 - -(2)
```
```
Table 2:Cluster rankings for features in the Caverlee 2011 data set
Rank has been marked as null(-) when the feature values for all the clusters were found to be very close/same.
In the case of foll-difference, clusters were first marked as having a positive or a negative difference, and then ranked.
```
```
Cluster No.of Bots following-count follower-count statuses-count len-name len-descr.
0 4101 5 5 5 - 5
2 3296 2 2 2 - 1
4 3362 4 4 4 - 3
5 3351 3 3 1 - 4
6 153 1 1 1 - 2
```
```
Table 3:Cluster rankings for features in the Caverlee 2019 data set
Rank has been marked as null(-) when the feature values for all the clusters were found to be almost the same.
```
```
Figure 2: Elbow Curve for Caverlee-
```
```
Figure 3: PCA 2-D Plot for Caverlee-
```
```
Figure 4: PCA 3-D Plot for Caverlee-
```
```
Figure 5: Elbow Curve for Caverlee-
```

Figure 6: PCA 2-D Plot for Caverlee-

Figure 7: PCA 3-D Plot for Caverlee-

## 6 Results

```
Caverlee-
Clustering on the Caverlee-2011 data set with the number of
clusters chosen using the elbow method produced 5 clusters,
labelled as 0,1,2,3, and 4.Cluster 0contained only outliers,
with just 2 bot accounts. Thus, we choose to ignore these
outliers and remove the cluster.
Among the remaining 4 clusters,Cluster 4contained bots
with the highest statuses count, while their followings counts
and followers counts were about normal; neither too high nor
too low. Also, these bots had a significantly larger number
of followers than the number of followings. Clearly, these
bots produce tweets to make content visible, and rely on their
popularity among the followers to spread the created content.
These bots can be identified as belonging to theSimple Bots
category as proposed by [Yan+19].
Cluster 2contained bot accounts with the highest following
counts, while their followers count and statuses counts were
not very different from bots belonging to other clusters.
Their following count, however, was significantly higher; it
was at least 200% higher than those of other bots. These
bots clearly correspond to theFake Followerscategory as
proposed by [Yan+19].
Cluster 3contained bots with a significantly low difference
between the number of followings and the number of follow-
ers. The difference on an average in this cluster was at least
than 50% lesser than the corresponding difference for bots
belonging to other clusters. They appear genuine, but exhibit
the reciprocity rule in their ”follow” relationships with other
accounts. Once they gain a good following, they begin to
post spam content and engage in malicious activities on
Twitter. These bots thus correspond to theFriend Infiltrators
category as proposed by [LEC11].
Cluster 1contained the largest number of bots, and these
exhibited interesting behavior. These bot accounts had the
lowest following counts, the lowest followers counts, and the
lowest statuses counts among all the clusters. They posted
statuses hardly accounting for 0.9% of the number of statuses
posted by theSimple Bots, and followed only about 3.38% of
the number of accounts that theFake Followers. They also
had only about 30% of the number of followers as theFriend
Infiltrators. Clearly, these bots have the least significant
activity on Twitter, neither engaging in the production and
spread of content, nor attempting to follow a large number of
accounts or gain a large number of followers. These bots can
be best categorized asDormant Bots, that remain inactive for
a majority of the time, until a certain event of interest occurs.
Then, they begin actively spreading content and performing
other potentially malicious activities.
In general, bots in theCaverlee-2011data set exhibited a
preference for following other users over gaining followers.
This is clearly shown by the fact that over 91.58% of the bots
had a positive difference between the number of followings
and the number of followers. This behavior is significantly
different from the behavior of bots in the Caverlee-2019 data
set, as we will see.
```

Caverlee-
K-Means Clustering on the Caverlee-2019 data set produced
unexpected results. While we expected to see clusters of bots
based on types such asFake Followers,Friend Infiltrators,
Simple Bots, and Dormant Bots, the clusters produced
separated bots on their degree of activity or involvement
online, where a higher number of followers/friends/tweets
indicate higher activity. Clusters 1 and 3contained only 5
and 2 bots respectively, and thus can be ignored as outliers.
Cluster 6contained 153 bots, and these exhibited the highest
activity. They had the highest numbers of followings, friends,
and statuses among all the bots in the data set.
Cluster 2contained 3296 bots, and these exhibited the
second highest level of activity.
Cluster 5contained 3351 bots, and these showed about
average activity or involvement online, either through tweets
produced or through the number of followers and friends
gained.
Cluster 4contained 3362 bots, and these showed mild
engagement online, significantly lower than the average bot
in the data set.
Cluster 0contained the largest number of bots, precisely
4101 of them. These bots were the most dormant of all the
bots, and showed least intent or activity. Relatively too, their
activity was much lower than all the other clusters together.
In comparison to the most active bots in Cluster 6, they
only had 0.78% of the number of followers, about 2.67% of
the number of friends, and a mere 1.27% of the number of
statuses or tweets.
In general, bots in the Caverlee-2019 data set had a very
high average number of followers, 14,958.34 to be precise.
The average number of friends was 4044.41, and the average
statuses count was found to be 10,143.54.

```
Comparisons: Caverlee-2011 vs Caverlee-
```
- Bots in the 2011 data set readily exhibited their intent
    and purpose through their activity footprint online. A
    simple comparison of their followers count, following
    count, and statuses count was enough to understand their
    intent and categorize them. Thus, they could easily be
    identified as belonging to a certain type of bots, and
    this made them vulnerable to bot detection algorithms.
    Bots in the 2019 data set however did not exhibit their
    real intentions at all, and maintained balanced levels of
    activity in terms of gaining followers, posting statuses,
    and following other accounts. This is the reason clus-
    tering on the 2019 data set separated bots on their levels
    of activity overall, rather than on their intended activity
    with respect to a particular feature. Also, a majority of
    them maintained subdued levels of involvement, making
    it harder for bot detection technologies to identify them
    based on their activity. This could be one reason they
    managed to get fool bot detection algorithms, and sur-
    vive from 2011 to 2019.
- Bots in the 2011 data set showed a preference for fol-
    lowing other users over gaining followers, and this was
    a vulnerability. Accounts following a large number of

```
users but not having many followers can be easily iden-
tified as bots. In the 2019 data set however, the aver-
age followers count was about 650% higher than that
of bots in 2011. While this could also be attributed to
the general increase in number of users on Twitter over
these years, it also shows a shift in the focus of the bots
from just following other users to also creating a large
follower base. This fulfils two purposes - one, these ac-
counts can be mistaken to be genuine accounts due to
their good number of followers and can thus fool de-
tection systems. Once they hoodwink the systems, they
have a good following and can then fulfil their actual
purpose - the spread of spam content through tweets and
retweets.
```
- Bots from the 2019 data set had a good number of
    friends - 4,044.41 on an average. Also, manual inspec-
    tion of certain bots with a large number of followers
    revealed that they maintained a minimum difference
    between the number of followers and followings.
    This behavior similar to the reciprocal behavior in the
    following-follower relationships exhibited byFriend
    Infiltratorscategory as proposed by [LEC11]. The
    reason the bots have taken to this behavior could be due
    to reason that these kinds of bots are difficult to identify
    during their initial stages, while they are merely gaining
    followers and following others without actually posting
    much content. This is another reason why these bots are
    still out there, surviving.

## References

```
[LEC11] Kyumin Lee, Brian Eoff, and James Caver-
lee. “Seven Months with the Devils: A Long-
Term Study of Content Polluters on Twitter”. In:
ICWSM. 2011.
[BF16] Alessandro Bessi and Emilio Ferrara. “Social
bots distort the 2016 U.S. Presidential elec-
tion online discussion”. In:First Monday21.
(2016).ISSN: 13960466.DOI: 10. 5210 / fm.
v21i11.7090.URL: https://firstmonday.org/ojs/
index.php/fm/article/view/7090.
[Dav+16] Clayton Allen Davis et al. “BotOrNot: A Sys-
tem to Evaluate Social Bots”. In:Proceedings
of the 25th International Conference Compan-
ion on World Wide Web. WWW ’16 Companion.
Montr&#233;al, Qu&#233;bec, Canada: Inter-
national World Wide Web Conferences Steering
Committee, 2016, pp. 273–274.ISBN: 978-1-
4503-4144-8.DOI: 10.1145/2872518.2889302.
URL: https://doi.org/10.1145/2872518.2889302.
[HK16] Philip N Howard and Bence Kollanyi. “Bots,#
StrongerIn, and# Brexit: computational propa-
ganda during the UK-EU referendum”. In:Avail-
able at SSRN 2798311(2016).
[HKW16] Philip N Howard, Bence Kollanyi, and Samuel
Woolley. “Bots and Automation over Twitter
during the US Election”. In:Computational Pro-
paganda Project: Working Paper Series(2016).
```

```
URL: http://geography.oii.ox.ac.uk/wp-content/
uploads / sites / 89 / 2016 / 11 / Data - Memo - US -
Election.pdf.
```
[Su ́a+16] Pablo Su ́arez-Serrato et al. “On the influence of
social bots in online protests”. In:International
Conference on Social Informatics. Springer.
2016, pp. 269–278.

[Møn+17] Bjarke Mønsted et al. “Evidence of complex
contagion of information in social media: An
experiment using Twitter bots”. In:PLOS ONE
12.9 (Sept. 2017), pp. 1–12.DOI: 10. 1371 /
journal. pone. 0184148.URL: https : / / doi. org /
10.1371/journal.pone.0184148.

[Sti+17] Stefan Stieglitz et al.Do Social Bots Dream
of Electric Sheep? A Categorisation of Social
Media Bot Accounts. 2017. arXiv: 1710. 04044
[cs.HC].

[18] Social Media Bots Overview. 2018.URL: https:
//www.dhs.gov/sites/default/files/publications/
190717 cisasocial-media-bots-overview.pdf.

[Yan+19] Kai-Cheng Yang et al. “Arming the public
with AI to counter social bots”. In: ArXiv
abs/1901.00912 (2019).



This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports
# Political-Bot-detection-and-Evolution
We will be analyzing how to detect the bots, in particular political bots and their evolution based on various social media tactics.
