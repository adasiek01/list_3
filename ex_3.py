def counting_chars_without_ifs(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read()
    char_count = {}
    for letter in text:
        letter.lower()
        amount = text.count(letter)
        char_count[letter] = amount
    return char_count


if __name__ == "__main__":
    print(counting_chars_without_ifs("L3_ZAD3_sample_text.txt"))
