%matplotlib inline
import os 
import re
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import requests

#config variables
user = "mentirozzo"

content=requests.get("https://overrustlelogs.net/Admiralbulldog%20chatlog/December%202019/userlogs/{}.txt".format(user)) 
content = content.text.split("\n")
messages = []
mal = 0
for line in content:
    x = re.match(r'^(\[.+\]) (.+): (.+)', line.strip())
    try:
        if x.group(2).lower() == user.lower():
            messages.append(x.group(3))
    except:
        mal += 1
print("Found {} malformed lines".format(mal))
res = ' '.join(messages)
wordcloud = WordCloud(min_font_size=20, max_font_size=100, max_words=70, background_color="white", width=1000, height=600, contour_color='red', stopwords=STOPWORDS).generate(res)
wordcloud.to_file("this.png")
# lower max_font_size
plt.figure(figsize=(10, 6), dpi = 100)
plt.title(user + " most common words for the month of December", backgroundcolor="white")
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
