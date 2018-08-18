# Twitter Data Analysis

### Sprint#3 (Aug 4, 2018, Sat)

* @Betül: Run Task1 (unique tweets) on all data (by Friday, Aug3)
* @Hamza: Take output from Task1 and run Task2 (retweet counts) on all unique tweets (by Saturday, Aug4)
* @ハン Keçeli規制 Han and @Burak Çolakoğlu: (Task3) Adopt Task2 code to find the other groups (Mention network - who mentioned who and how many times) (by Saturday, Aug4)

### Task1: Unique tweets
We collected tweets using two developer accounts. Therefore, we need to filter duplicate tweets.

Run:
* pyspark rmvDuplicates.py

### Task2: Retweet network
Find users who retweet each other and the number of retweets (user1, user2, count).

Run:
* pyspark retweetNetwork.py

### Task3: Mention network
Find users who mentioned other users and the number of tweets that mention the other user (user1, user2, count).

Run:
* pyspark mentionNetwork.py


### Papers:
Examining trolls and polarization with a retweet network
LG Stewart, A Arif, K Starbird - … Mining on the Web 2018
http://faculty.washington.edu/kstarbi/examining-trolls-polarization.pdf
