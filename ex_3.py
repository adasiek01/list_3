def counting_chars_without_ifs(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.replace(' ', '') for line in lines]
    with open(filename, 'w') as f:
        f.writelines(lines)
    file_ref = open(filename, 'r')
    text = file_ref.read()
    small_text = text.lower()
    char_count = {}
    for letter in small_text:
        amount = small_text.count(letter)
        char_count[letter] = amount
    return char_count


if __name__ == "__main__":
    print(counting_chars_without_ifs("L3_ZAD3_sample_text.txt"))
