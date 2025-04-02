from tokenizer import tokenize
from read import read_texts_from_folder
from utils import merge_texts
from analyzer import get_top_terms
from analyzer import analyze_tokens
from utils import get_stopwords



if __name__ == "__main__":
    texts = read_texts_from_folder("data")
    full_text = merge_texts(texts)
    all_tokens = tokenize(full_text)
    print(all_tokens)

    stop_words = get_stopwords()
    stats = analyze_tokens(all_tokens, stop_words)

    print("Total terms: ", stats["total_terms"])
    print("Unique terms: ", stats["unique_terms"])
    print("Term frequency: ", stats["term_freq"])
    print("Stopword count: ", stats["stopword_count"])

    print("Top 50 terms with stopwords: ", get_top_terms(stats["term_freq"]))
    print("Top 50 terms without stopwords: ", get_top_terms(stats["term_freq"], stop_words))