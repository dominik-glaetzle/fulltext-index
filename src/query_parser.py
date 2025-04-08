from tokenizer import preprocess

def parse_query(query):
    return preprocess(query, True, True, True)


def load_queries_from_csv(path="../data/queries.csv"):
    queries = []
    with open(path, "r", encoding="utf-8") as csv:
        for line in csv:
            parts = line.strip().split('","')
            query = parts[0].strip('"')
            queries.append(query)
    return queries
