def transform(text):
    text_list = list(text)
    for i, char in enumerate(text_list):
        if char in ALPHABET:
            text_list[i] = ALPHABET.index(char)
    return text_list

def crypt(text, key):
    text = transform(text)
    text = [(n + key) % 26 if type(n) == int else n for i, n in enumerate(text)]
    return text

def decrypt(text, key):
    text = transform(text)
    decrypted = []
    if key is None:
        for k in range(26):
            decrypted.append(crypt(text, -k))
        text = decrypted
        return text
    else:
        return crypt(text, -key)

def caesar(text, key, mode):
    result = []
    if mode:
        text = crypt(text, key)
    else:
        text = decrypt(text, key)
    for i, char in enumerate(text):
        if type(char) == int:
            text[i] = ALPHABET[char]
        elif type(char) == list:
            for j, sub_char in enumerate(char):
                if type(sub_char) == int:
                    char[j] = ALPHABET[sub_char]
            value = ''.join(char)
            result.append(f'==> key = {i} : {value}')
    if len(result) != 0:
        return '\n'.join(result)
    return f"==> {''.join(text)}"

ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

if input('==> Encrypt or Decrypt ? : ').lower() == 'encrypt':
    text = input('Enter what you want to encrypt => ').upper()
    key = int(input('Enter the key  [0-25] => '))
    mode = True
else:
    text = input('Enter what you want to decrypt => ').upper()
    if input('Do you have the key ? (y/n) :').lower() == 'y':
        key = int(input('Enter the key => '))
    else:
        key = None
    mode = False

print(caesar(text, key, mode))
