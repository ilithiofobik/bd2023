from processing import *

if __name__ == "__main__":
    poem = read_poem("hamlet")
    poem = clean_poem(poem)
    poem = poem_to_words(poem)
    poem = remove_stop_words(poem)
    poem = frequency(poem)
    poem = sort_by_frequency(poem)
    write_to_word_cloud(poem)