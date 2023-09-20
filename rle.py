def run_length_encode_file(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    
    encoded_text = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded_text += str(count) + text[i - 1]
            count = 1
    encoded_text += str(count) + text[-1]
    
    with open(output_file, 'w') as f:
        f.write(encoded_text)

# Usage
input_file = 'input.txt'
output_file = 'rle_encoded.txt'
run_length_encode_file(input_file, output_file)
