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

def text_to_list_of_words(text: str):
    poem = clean_poem(text)
    poem = poem_to_words(poem)
    return remove_stop_words(poem)

def poem_to_list_of_words(name: str):
    poem = read_poem(name)
    return text_to_list_of_words(poem)