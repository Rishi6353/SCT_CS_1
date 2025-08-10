# Caesar Cipher Program

def caesar_cipher(text, shift, mode):
    result = ""
    
    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Only shift letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-letters unchanged
    return result

# Main program
message = input("Enter your message: ")
shift = int(input("Enter shift value (0-25): "))
mode = input("Choose mode - encrypt or decrypt: ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
else:
    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")
