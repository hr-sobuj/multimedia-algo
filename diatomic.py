import base64

# Function to encode data using base64
def base64_encode(data):
    encoded_bytes = base64.b64encode(data.encode())
    encoded_data = encoded_bytes.decode()
    return encoded_data

# Function to decode data using base64
def base64_decode(encoded_data):
    decoded_bytes = base64.b64decode(encoded_data)
    decoded_data = decoded_bytes.decode()
    return decoded_data

# Reading input from input.txt
try:
    with open("input.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("input.txt not found. Please create the file and place your input data in it.")
    exit(1)

# Encoding and writing to encoded_output.txt
encoded = base64_encode(data)
with open("encoded_output.txt", "w") as encoded_file:
    encoded_file.write(encoded)
print("Encoded data written to encoded_output.txt")
