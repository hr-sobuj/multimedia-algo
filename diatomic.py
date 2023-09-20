frequent_words = ['Th', 'is', 'a ', 'to', 'of', 'in', 'ed', 'oo', 'el', 'li']
replace_chars = ['@', '$', '%', '^', '&', '*', '_', '+', ';', '|']


def diatomic_encoding(message):
    encoded_text = ""
    length = len(message) - 1
    i = 0

    while i < length:
        if i + 1 <= length:
            temp = message[i] + message[i + 1]
            if temp in frequent_words:
                encoded_text = encoded_text + (replace_chars[frequent_words.index(temp)])
                i = i + 2
                continue
            else:
                encoded_text = encoded_text + message[i]
        else:
            encoded_text = encoded_text + message[i]
        i = i + 1

    print(encoded_text)


msg = "This is a demo text to encoded"
diatomic_encoding(msg)
