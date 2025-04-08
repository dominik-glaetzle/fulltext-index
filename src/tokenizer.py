import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from utils import get_stopwords

nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("wordnet")

EN_STOPWORDS = get_stopwords()
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess(text, remove_stopwords = False, stemming = False, lemmatization = False):
    text = text.lower()
    tokens = word_tokenize(re.sub(r"[^\w\s]", "", text))

    if remove_stopwords:
        tokens = [t for t in tokens if t not in EN_STOPWORDS]

    if stemming:
        tokens = [stemmer.stem(t) for t in tokens]

    if lemmatization:
        tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return tokens
