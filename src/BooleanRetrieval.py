from query_parser import parse_query

class BooleanRetrieval:
    def __init__(self, inverted_index):
        self.index = inverted_index.index

    def search(self, query):
        query_tokens = parse_query(query)
        print(f"query tokens ({len(query_tokens)}): ", query_tokens)
        if not query_tokens:
            return []
        
        # step 1: documents with at least one token
        docs = set()
        for token in query_tokens:
            docs |= self.index.get(token, set())

        # step 2: sim(q,d) = |q ∩ d| / |q|
        
        results = []
        for doc_id in docs:
            doc_terms = {term for term in self.index if doc_id in self.index[term]}
            common_terms = set(query_tokens) & doc_terms
            score = len(common_terms) / len(query_tokens)
            results.append((doc_id, score))

        # step 3: sort for score
        results.sort(key=lambda x: x[1], reverse=True)
        return results