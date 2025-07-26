def encode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result

def decode(message, shift):
    return encode(message, -shift)

# Example usage
if __name__== "_main_":
    msg = "Hello World"
    shift = 3
    encrypted = encode(msg, shift)
    decrypted = decode(encrypted, shift)
    print("Encoded:", encrypted)
    print("Decoded:", decrypted)