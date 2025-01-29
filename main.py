def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        count_words()
        count_chars()

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        print(word_count)

def count_chars():
    chars = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        
        for char in file_contents:
            chars.setdefault(char, 0)
            chars[char] += 1
    
    print(chars)
main()