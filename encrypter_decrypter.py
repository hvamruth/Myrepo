from cryptography.fernet import Fernet
import os
import sys


def generate_key():
    """Generate a random encryption key."""
    return Fernet.generate_key()


def load_key(key_file):
    """Load the encryption key from a file."""
    with open(key_file, "rb") as file:
        key = file.read()
    return key


def save_key(key, key_file):
    """Save the encryption key to a file."""
    with open(key_file, "wb") as file:
        file.write(key)


def encrypt_file(key, input_file, output_file):
    """Encrypt the input file and save the encrypted data to the output file."""
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(output_file, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(key, input_file, output_file):
    """Decrypt the input file and save the decrypted data to the output file."""
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    # Generate or load the encryption key
    key_file = "encryption.key"
    if not os.path.isfile(key_file):
        key = generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)

    # Encrypt or decrypt the file based on command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python encrypt_decrypt_tool.py <encrypt|decrypt> <input_file> <output_file>")
        sys.exit(1)

    action = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if action == "encrypt":
        encrypt_file(key, input_file, output_file)
        print("File encrypted successfully.")
    elif action == "decrypt":
        decrypt_file(key, input_file, output_file)
        print("File decrypted successfully.")
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
