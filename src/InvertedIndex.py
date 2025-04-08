import json
from collections import defaultdict
from tokenizer import preprocess

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)
        self.doc_count = 0

    def add_doc(self, doc_id, text):
        tokens = preprocess(text, True, True, True)
        for token in tokens:
            self.index[token].add(doc_id)
        self.doc_count += 1

    def write_to_disk(self, index_path="../data/index.json", stats_path="../data/stats.json"):
        serializable_index = {term: list(postings) for term, postings in self.index.items()}
        with open(index_path, 'w') as f:
            json.dump(serializable_index, f)
        with open(stats_path, 'w') as f:
            json.dump({
                "doc_count": self.doc_count,
                "unique_terms": len(self.index)
            }, f)

    def load_from_disk(self, index_path="../data/index.json", stats_path="../data/stats.json"):
        with open(index_path, 'r') as f:
            raw_index = json.load(f)
            self.index = {term: set(postings) for term, postings in raw_index.items()}
        with open(stats_path, 'r') as f:
            stats = json.load(f)
            self.doc_count = stats["doc_count"]