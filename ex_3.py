def counting(title):
    o = open(title, "r")
    text = o.read()
    dict_1 = {}
    for letter in text:
        amount = text.count(letter)
        dict_1[letter] = amount
    return dict_1


if __name__ == "__main__":
    print(counting("aaa.txt"))
