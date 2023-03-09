import io
import re 

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

def write_to_word_cloud(freq: list):
    with open("data/word_cloud.csv", "w") as f:
        for i in range(0, 100):
            (word, count) = freq[i]
            f.write(str(count) + ";\"" + word + "\";\"\";\"\"\n")