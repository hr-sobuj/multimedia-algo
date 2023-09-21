diatomic_dict = {}

def add_diatomic_mapping(word, replacement):
    diatomic_dict[word] = replacement

def diatomic_encoding(message):
    encoded_text = ""
    length = len(message) - 1
    i = 0

    while i < length:
        if i + 1 <= length:
            temp = message[i:i + 2]
            if temp in diatomic_dict:
                encoded_text += diatomic_dict[temp]
                i += 2
                continue
            else:
                encoded_text += message[i]
        else:
            encoded_text += message[i]
        i += 1

    return encoded_text

def load_mappings_from_file(mapping_file):
    with open(mapping_file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            add_diatomic_mapping(parts[0], parts[1])

if __name__ == "__main__":
    mapping_file_name = "mappings.txt"
    input_file_name = "input.txt"

    load_mappings_from_file(mapping_file_name)

    with open(input_file_name, 'r') as input_file:
        input_text = input_file.read()

    encoded_text = diatomic_encoding(input_text)
    print(encoded_text)
