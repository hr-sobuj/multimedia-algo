def lzw_encode_file(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    
    dictionary = {chr(i): i for i in range(256)}
    result = []
    current = ""
    
    for char in text:
        current += char
        if current not in dictionary:
            dictionary[current] = len(dictionary)
            result.append(dictionary[current[:-1]])
            current = char
    result.append(dictionary[current])
    
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, result)))

# Usage
input_file = 'input.txt'
output_file = 'lzw_encoded.txt'
lzw_encode_file(input_file, output_file)
