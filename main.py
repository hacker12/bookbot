#!/usr/bin/env python3

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        print_report(file_contents, path_to_file)

def caracter_occurrences(file_contents):
    # Count the number of times each character appears in the text
    character_counts = {}
    # make the string lowercase
    file_contents = file_contents.lower()
    for character in file_contents:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    # sort by alphabetical order
    character_counts = dict(sorted(character_counts.items()))

    return character_counts

def word_count(file_contents):
    # Count the number of words in the text
    return len(file_contents.split())

def print_occurrences(character_counts):
    # Print the number of times each character appears in the text
    for character, count in character_counts.items():
        print(f"The '{character}' charcter was found {count} times")

def print_report(file_contents, path_to_file):
    
    wc = word_count(file_contents)
    character_counts = caracter_occurrences(file_contents)

    print (f"--- Begin report of {path_to_file} ---")
    print(f"{wc} words found in the document")
    print(" ")
    print_occurrences(character_counts)
    print("--- End of report ---")

if __name__ == "__main__":
    main()