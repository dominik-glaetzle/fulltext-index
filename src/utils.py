from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")


def merge_texts(texts):
    return " ".join(texts)

def get_stopwords():
    return set(stopwords.words("english"))