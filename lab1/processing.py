import io
import re 
import math

def read_stop_words():
    stop_words = []
    with open("data/stop_words_english.txt") as f:
        for line in f:
            stop_words.append(line.strip())
    return stop_words

def read_poem(name: str):
    filename = "data/" + name + ".txt"
    f = io.open(filename, mode="r", encoding="utf-8")
    text = f.read()
    return text.lower()

def clean_poem(poem: str):
    poem = re.sub('[^a-z0-9]+', ' ', poem)
    poem = poem.replace("\n", ' ')
    poem = poem.replace("\r", ' ')
    return poem

def poem_to_words(poem: str):
    return poem.split()

def remove_stop_words(words: list):
    stop_words = read_stop_words()
    return [word for word in words if word not in stop_words and len(word) > 2]

def frequency(words: list) -> dict:
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def sort_by_frequency(freq: dict):
    return [(word, count) for [word, count] in sorted(freq.items(), key=lambda x: x[1], reverse=True)]

def sort_by_freq_list(freq: list):
    return [(word, count) for (word, count) in sorted(freq, key=lambda x: x[1], reverse=True)]


def poem_to_list_of_words(name: str):
    poem = read_poem(name)
    poem = clean_poem(poem)
    poem = poem_to_words(poem)
    poem = remove_stop_words(poem)
    poem = frequency(poem)
    return sort_by_frequency(poem)

def write_to_word_cloud(freq: list, title: str):
    with open("data/" + title + ".csv", "w") as f:
        for i in range(0, 100):
            (word, count) = freq[i]
            f.write(str(count) + ";\"" + word + "\";\"\";\"\"\n")

def list_contains(list: list, word: str):
    for (w, _) in list:
        if w == word:
            return True
    return False

def tf_idf_of_poems(names: list):
    D = {}
    for name in names:
        D[name] = poem_to_list_of_words(name)
    for name, d in D.items():
        all_words_num = sum([count for (_, count) in d])
        tf_idfs = []
        for (word, count) in d:
            tf = count / all_words_num
            idf = math.log(len(D) / sum([1 for _, d in D.items() if list_contains(d, word)]))
            tf_idf = tf * idf
            tf_idf = int(1_000_000_000 * tf_idf)
            tf_idfs.append((word, tf_idf))
        tf_idfs = sort_by_freq_list(tf_idfs)
        write_to_word_cloud(tf_idfs, name + "_tf_idf")



        

