class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) - self.key
                if char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                elif char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text

cipher = CaesarCipher(3)
encrypted_text = "sayaka"
decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text)
