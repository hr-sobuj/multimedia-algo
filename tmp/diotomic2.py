def diatomic_encode(data):
    encoded_data = ""
    for i in range(len(data)):
        encoded_data += chr(ord(data[i]) + 128)
    return encoded_data

def diatomic_decode(encoded_data):
    decoded_data = ""
    for i in range(len(encoded_data)):
        decoded_data += chr(ord(encoded_data[i]) - 128)
    return decoded_data

# Reading input from input.txt
try:
    with open("input.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("input.txt not found. Please create the file and place your input data in it.")
    exit(1)

# Encoding and writing to encoded_output.txt
encoded = diatomic_encode(data)
with open("encoded_output.txt", "w") as encoded_file:
    encoded_file.write(encoded)
print("Encoded data written to encoded_output.txt")

# Decoding and writing to decoded_output.txt
try:
    with open("encoded_output.txt", "r") as encoded_file:
        encoded_data = encoded_file.read()
    decoded = diatomic_decode(encoded_data)
    with open("decoded_output.txt", "w") as decoded_file:
        decoded_file.write(decoded)
    print("Decoded data written to decoded_output.txt")
except FileNotFoundError:
    print("encoded_output.txt not found. Please encode the input data first.")
