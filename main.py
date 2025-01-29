def main():
        write_report(count_words(), count_chars())

def sort_on(dict):
    return dict["num"]

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count

def count_chars():
    chars = []

    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        
        for char in file_contents:
            found = False
            if char.isalpha():
                for dict in chars:
                    if dict["char"] == char:
                        dict["num"] += 1
                        found = True
                        break
                
                if not found:
                    chars.append({"char": char, "num": 1})
    
    chars.sort(reverse=True, key=sort_on)
    return chars

def write_report(word_count, char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()

    for char_dict in char_list:
        print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")

    print("--- End report ---")
main()