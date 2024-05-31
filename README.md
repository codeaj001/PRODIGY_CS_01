# Caesar Cipher Program

## How the Program Works:

1. **`caesar_cipher` Function** 🛠️:
   - This function takes the **text**, the **shift value**, and the **direction** (either **'encrypt'** 🔐 or **'decrypt'** 🔓). It processes each character:
     - If the character is **alphabetic** 🔤, it shifts it by the given number of positions 🔄.
     - If the direction is **'decrypt'** 🔓, it negates the shift value 🔁.
     - **Non-alphabetic characters remain unchanged** 🚫.

2. **`main` Function** 🖥️:
   - This function provides the **user interface** 👤:
     - It prompts the user to choose between **encryption and decryption** ❓.
     - It collects the **message** 📝 and the **shift value** 🔢 from the user.
     - It calls the `caesar_cipher` function with the provided inputs and **displays the result** 📜.
     - It asks the user if they want to perform another operation 🔁.

## Example Usage:

- If the user inputs **"encrypt"** 🔐, the message **"Hello, World!"** 📝 and the shift value **"3"** 🔢, the output will be **"Khoor, Zruog!"** 🌐.
- If the user inputs **"decrypt"** 🔓, the message **"Khoor, Zruog!"** 📝 and the shift value **"3"** 🔢, the output will be **"Hello, World!"** 🌍.

This program will **repeatedly prompt the user until they choose to stop** ✋, making it **user-friendly** for multiple encryption and decryption operations.
