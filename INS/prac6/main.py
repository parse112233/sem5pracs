# AES Encryption and Decryption
import pyaes

key = b"This_key_for_demo_purposes_only!"
pt = "Encrypt this string"

# Encryption

aes = pyaes.AESModeOfOperationCTR(key)
cipher = aes.encrypt(pt)
print("Cipher: ", cipher)

# Decryption
aes = pyaes.AESModeOfOperationCTR(key)
decrypt = aes.decrypt(cipher)
print("Plain Text: ", decrypt)