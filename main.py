file_path = "books/frankenstein.txt"

def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_book_word_count (file_contents):
    words_list = file_contents.split()
    num_words = len(words_list)
    return num_words

def main ():
    print (f"{get_book_word_count(file_contents= get_book_text(file_path))} words found in the document");
    
    
main();