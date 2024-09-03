import string
import os

def process_file(fname, enc):
    with open(fname, 'r', encoding=enc) as file:
        data = file.read()
    return data.split()


def write_results(fname, data, enc):
    with open(fname, 'w', encoding=enc) as file:
        file.write(data)

def words_to_dict(all_words, dictionary):
    for w in all_words:
        w = clean_word(w)
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1


def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")
    word = word.lower()  # Convert to lowercase for case-insensitive comparison
    return word


def calculate_ttr(word_dict):
    total_words = sum(word_dict.values())
    unique_words = len(word_dict)
    ttr = unique_words / total_words if total_words > 0 else 0
    return ttr, total_words, unique_words


def search_word_in_text(word, word_dict):
    return word_dict.get(word, 0)


def main():
    books = [
        "A Book of Ghosts.txt",
        "Alice's Adventures in Wonderland.txt",
        "Stories of Christmas and the Bowie Knife.txt",
        "DRACULA.txt",
        "Up in Ardmuirland.txt"
    ]
    
    print("Available texts:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
    
    # User selects two texts to compare
    first_choice = int(input("Choose the first text (1-5): ")) - 1
    second_choice = int(input("Choose the second text (1-5): ")) - 1
    
    first_text = books[first_choice]
    second_text = books[second_choice]
    
    # Process the selected texts
    first_words = process_file(first_text, 'utf-8')
    second_words = process_file(second_text, 'utf-8')
    
    first_dict = {}
    second_dict = {}
    
    words_to_dict(first_words, first_dict)
    words_to_dict(second_words, second_dict)
    
    # Calculate TTR
    first_ttr, first_total, first_unique = calculate_ttr(first_dict)
    second_ttr, second_total, second_unique = calculate_ttr(second_dict)
    
    # Display the statistics
    print(f"\nStatistics for {first_text}:")
    print(f"Total words: {first_total}")
    print(f"Unique words: {first_unique}")
    print(f"TTR: {first_ttr:.4f}")
    
    print(f"\nStatistics for {second_text}:")
    print(f"Total words: {second_total}")
    print(f"Unique words: {second_unique}")
    print(f"TTR: {second_ttr:.4f}")
    
    # Compare TTRs
    if abs(first_total - second_total) > 3000:
        print("\nNote: The word count difference between the texts is more than 3000, which might affect the reliability of the TTR comparison.")
    
    # Word search functionality
    search_word = clean_word(input("\nEnter a word to search for: "))
    first_word_count = search_word_in_text(search_word, first_dict)
    second_word_count = search_word_in_text(search_word, second_dict)
    
    if first_word_count > 0:
        print(f"'{search_word}' found {first_word_count} time(s) in {first_text}.")
    else:
        print(f"'{search_word}' not found in {first_text}.")
    
    if second_word_count > 0:
        print(f"'{search_word}' found {second_word_count} time(s) in {second_text}.")
    else:
        print(f"'{search_word}' not found in {second_text}.")


if __name__ == "__main__":
    main()
