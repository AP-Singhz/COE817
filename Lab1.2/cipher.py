def vigenere_encrypt(text, key):
    key = key.upper()
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    key = key.upper()
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text
