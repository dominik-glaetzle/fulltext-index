from collections import Counter
from tokenizer import preprocess

def analyze_tokens(tokens, stopwords):
    token_amount = len(tokens)
    unique_terms = len(set(tokens))
    term_freq = Counter(tokens)
    stopword_count = 0
    for t in tokens:
        if t in stopwords:
            stopword_count += 1

    return {
        "total_terms": token_amount,
        "unique_terms": unique_terms,
        "term_freq": term_freq,
        "stopword_count": stopword_count
    }

def get_top_terms(freq_counter, stopwords_set=None, top_n=50):

    filtered_items = []

    for word, count in freq_counter.items():
        if stopwords_set and word in stopwords_set:
            continue

        filtered_items.append((word, count))

    sorted_items = sorted(filtered_items, key=lambda item: item[1], reverse=True)

    return sorted_items[:top_n]

def get_preprocessing_stats(text):
    return {
        "original": len(preprocess(text)),
        "only-removed-stopwords": len(preprocess(text, True)),
        "removed-stopwords+stemming": len(preprocess(text, True, True)),
        "removed-stopwords+stemming+lemmatization": len(preprocess(text, True, True, True)),
    }