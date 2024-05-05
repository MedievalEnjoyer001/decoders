class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def decrypt(self, text):
        key_length = len(self.key)
        decrypted_text = ""

        for i in range(len(text)):
            char = text[i]
            key_char = self.key[i % key_length]

            if char.isalpha():
                shift = ord(key_char.lower()) - ord('a')
                if char.islower():
                    decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                else:
                    decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += char

        return decrypted_text

# Example usage
key = "sayaka"
cipher = VigenereCipher(key)
encrypted_text = "hinata"
decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text)
