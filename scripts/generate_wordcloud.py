import re
from sys import argc, argv, exit
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import requests


def generate_wordcloud(user: str) -> None:
    """Given a username, search admiralbulldog's channel logs for messages submitted by this user, and render them as a word cloud.

    Args:
        user (str): Twitch username whose naughty history will be made clear
    """

    # Grab a user's logs for a specific month and year
    # TODO allow user to specify month and year, currently hardcoded
    content = requests.get(
        "https://overrustlelogs.net/Admiralbulldog%20chatlog/December%202019/userlogs/{}.txt".format(
            user
        )
    )
    content = content.text.split("\n")

    messages = []
    malformed_counter = 0
    for line in content:
        # TODO document this
        x = re.match(r"^(\[.+\]) (.+): (.+)", line.strip())
        try:
            if x.group(2).lower() == user.lower():
                messages.append(x.group(3))
        except:
            malformed_counter += 1

    print(f"Found {malformed_counter} malformed line(s) that are henceforth ignored")
    res = " ".join(messages)
    wordcloud = WordCloud(
        min_font_size=20,
        max_font_size=100,
        max_words=70,
        background_color="white",
        width=1000,
        height=600,
        contour_color="red",
        stopwords=STOPWORDS,
    ).generate(res)
    wordcloud.to_file(f"{user}_wordcloud.png")

    # Render it all on screen
    plt.figure(figsize=(10, 6), dpi=100)
    plt.title(
        f"{user}'s most common words for the month of December", backgroundcolor="white"
    )
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    # Blocks until shut down
    plt.show()


if __name__ == "__main__":
    if len(argc) != 2:
        print("Usage: python[3] generate_wordcloud.py <USERNAME>")
        exit(1)
    generate_wordcloud(argv[1])
