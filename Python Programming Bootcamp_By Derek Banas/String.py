str_original = "Random Access Memory"
str_encrypted = ""

for char in str_original:
    if char != " ":
        char = chr(ord(char) + 3)
    
    str_encrypted += char


print(str_encrypted)

str_decrypted = ""

for char in str_encrypted:
    if char != " ":
        char = chr(ord(char) - 3)
    
    str_decrypted += char

print(str_decrypted)