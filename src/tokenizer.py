import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download('punkt_tab')

def tokenize(text):
    text = re.sub(r"[^\w\s]", "", text.lower())
    return word_tokenize(text)