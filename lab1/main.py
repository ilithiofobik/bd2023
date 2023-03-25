from processing import *
from bloom import *

if __name__ == "__main__":
    poem = [word for (word, _) in poem_to_list_of_words("hamlet")]
    bloom_exp(poem)
