import csv
import random
import numpy as np
from processing import poem_to_list_of_words

def rand_vecs(n):
    return [ [random.choice([-1.0, 1.0]) for _ in range(n)] for _ in range(1024) ]

def cosine_dist(v1, v2):
    return np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def cosine_sign(drama, vectors):
    drama_counts = { word: 0 for word in all_words }
    for word in words_lists[drama]:
        drama_counts[word] += 1
    drama_counts = np.array([ drama_counts[word] for word in all_words ])
    return [ np.sign(np.dot(vector, drama_counts)) for vector in vectors ]

if __name__ == "__main__":
    dramas = ["hamlet", "KingLear", "Othello", "RomeoJuliet", "ulysses_chapter1" ]
    num_of_dramas = len(dramas)

    words_lists = { drama: poem_to_list_of_words(drama) for drama in dramas }
    all_words = set()
    for drama in dramas:
        all_words = all_words.union(set(words_lists[drama]))

    all_words = list(all_words)
    vectors = rand_vecs(len(all_words))
    cosine_signature = { drama: cosine_sign(drama, vectors) for drama in dramas }

    for i in range(num_of_dramas - 1):
        for j in range(i + 1, num_of_dramas):
            drama1 = dramas[i]
            drama2 = dramas[j]
            print("{}, {}: {}"
                .format(
                    drama1,
                    dramas[j],
                    cosine_dist(
                        cosine_signature[drama1], 
                        cosine_signature[drama2]
                    )
                )
            )