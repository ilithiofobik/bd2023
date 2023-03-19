from processing import *

if __name__ == "__main__":
    poem = poem_to_list_of_words("hamlet")
    write_to_word_cloud(poem, "hamlet_normal")

    poems = [
        "hamlet", 
        "Othello", 
        "RomeoJuliet", 
        "KingLear"
    ]

    tf_idf_of_poems(poems)