def caesar_cipher(text, shift, direction):
    result = ""

    if direction == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

def main():
    print("Caesar Cipher")
    while True:
        direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
        if direction not in ["encrypt", "decrypt"]:
            print("Invalid choice, please type 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter your message: ").strip()
        shift = int(input("Enter the shift value: ").strip())

        if shift < 0:
            print("Shift value should be a non-negative integer.")
            continue

        result = caesar_cipher(text, shift, direction)
        print(f"The {direction}ed text is: {result}")

        again = input("Do you want to go again? (yes/no): ").strip().lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()
