import mmh3
import os
from sklearn.cluster import KMeans
from processing import text_to_list_of_words

# zadanie 35
def min_hash(L, hs):
    return [ min(h(x) for x in L) for h in hs ]

# zadanie 36
def k_grams(X, k):
    return { ''.join(map(str, X[i:i + k])) for i in range(len(X) - k) }

# min{h(y): y\in X^(k)}
def k_gram_min(X, k, h):
    return min(h(y) for y in k_grams(X, k))

def get_min_hash_vec(X, n):
    k_grams7 = k_grams(X, 7)
    hs = [ (lambda x: mmh3.hash(x, i)) for i in range(n) ]
    return min_hash(k_grams7, hs)

def jackard(A, B, k):
    A = k_grams(A, k) 
    B = k_grams(B, k)
    return len(A.intersection(B)) / len(A.union(B))

def approx(a_vec,  b_vec, n) -> float:
    return sum(1 for a, b in zip(a_vec, b_vec) if a == b) / n

def get_documents():
    documents = {}
    for file in os.listdir("chapters"):
        if file.endswith(".txt"):
            with open("chapters/" + file, "r") as f:
                documents[file] = text_to_list_of_words(f.read())
    return documents

def print_clusters(k, min_hashes, keys):
    print(f"{k} clusters:")
    kmeans = KMeans(n_clusters=k).fit(list(min_hashes.values()))
    labels = kmeans.labels_
    for i, key in enumerate(keys):
        print(key, labels[i])

if __name__ == "__main__":
    documents = get_documents()
    num_of_docs = len(documents)
    keys = list(documents.keys())
    key_pairs = [ (keys[i], keys[j]) for i in range(num_of_docs) for j in range(i + 1, num_of_docs) ]

    for n in [64, 128, 256]:
        print(f'n: {n}')

        min_hashes = { key : get_min_hash_vec(doc, n) for (key, doc) in documents.items() }

        for (key1, key2) in key_pairs:
            jackard_exact   = jackard(documents[key1], documents[key2], 7)
            if jackard_exact > 0.0:
                jackard_approx = approx(min_hashes[key1], min_hashes[key2], n)
                print((key1, key2), ": ", jackard_exact, jackard_exact)                       

        # szekspir vs ulysses
        print_clusters(2, min_hashes, keys)
        # każdy dokument osobno 
        print_clusters(5, min_hashes, keys)