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

# User input for encoding
data = input("Enter the data to encode: ")
encoded = diatomic_encode(data)
print("Encoded:", encoded)

# User input for decoding
encoded_data = input("Enter the data to decode: ")
decoded = diatomic_decode(encoded_data)
print("Decoded:", decoded)
