y = open('project_twitter_data.csv','r')
lines_lst = y.readlines()
tweets_lst = []
for i in lines_lst[1:] :
    tweets_lst = tweets_lst + [i.split(',')[0]]
#print(tweets_lst[0:3])
n_retweets = []
n_replies = []
for i in lines_lst[1:]:
    n_retweets = n_retweets + [i.split(',')[1]]
    n_replies = n_replies + [i.split(',')[2][0]]
print(n_retweets)
print(n_replies)
y.close()

def strip_punctuation(x):
    for i in punctuation_chars:
        x = x.replace(i,'')
    return x

def get_pos(x):
    y = x.split()
    z = 0
    for i in y :
        if strip_punctuation(i).lower() in positive_words:
            z = z + 1
    return z

def get_neg(x):
    y = x.split()
    z = 0
    for i in y :
        if strip_punctuation(i).lower() in negative_words:
            z = z + 1
    return z

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

p_scores = []
n_scores = []
for i in tweets_lst :
    p_scores = p_scores + [get_pos(i)]
    n_scores = n_scores + [get_neg(i)]
#print(p_scores)
#print(n_scores)

y = open('resulting_data.csv','w')
y.write('{},{},{},{},{}'.format('Number of Retweets',' Number of Replies',' Positive Score',' Negative Score',' Net Score\n'))
for i in range(len(p_scores)):    
    y.write('{},{},{},{},{}{}'.format(n_retweets[i],n_replies[i],p_scores[i],n_scores[i],p_scores[i]-n_scores[i],'\n'))
print(open('resulting_data.csv','r').readlines())
y.close()
