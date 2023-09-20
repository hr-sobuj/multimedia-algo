def lzw_encode(text):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    current = ""
    code = 256

    for char in text:
        current += char
        if current not in dictionary:
            dictionary[current] = code
            code += 1
            result.append(dictionary[current[:-1]])
            current = char

    result.append(dictionary[current])
    
    return result

def lzw_decode(encoded_data):
    dictionary = {i: chr(i) for i in range(256)}
    code = 256
    result = [dictionary[encoded_data[0]]]
    current = dictionary[encoded_data[0]]

    for next_code in encoded_data[1:]:
        if next_code in dictionary:
            entry = dictionary[next_code]
        elif next_code == code:
            entry = current + current[0]
        else:
            raise ValueError("Invalid LZW code")

        result.append(entry)
        dictionary[code] = current + entry[0]
        code += 1
        current = entry

    return ''.join(result)

# Usage
input_text = "BAABABBBAABBBBAA"
encoded_data = lzw_encode(input_text)
decoded_text = lzw_decode(encoded_data)

print("Encoded Data:", encoded_data)
print("Decoded Text:", decoded_text)
