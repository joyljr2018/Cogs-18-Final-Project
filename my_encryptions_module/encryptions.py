# key encryption from the class


def key_encryption(key,message):
    encoded = ''
    for char in message:
        encoded = encoded +  chr(ord(char) + key)
    return encoded

# decrption function for the key encryption 
def key_decryption(key,message):
    decoded = ''
    for char in message:
        decoded = decoded +  chr(ord(char) - key)
    return decoded


# caesar encryption 
def encryptcaesar(key,message):
    message = str(message).upper()
    key=str(key)
    encoded = ''.join([chr(97 + (ord(i) + ord(key.upper()))% 26) for i in message])
    return encoded

def decryptcaesar(key,message):
    message = str(message).upper()
    key = str(key)
    decoded = ''.join([chr(97 + (ord(i) - ord(key.upper()))% 26)  for i in message])
    return decoded

def vigenere_encryption(key,message):
    #getting rid of the spaces
    message.replace(" ","")
    encoded = ''
    keylength = len(key)
    for i in range(len(message)):
        encoded += encryptcaesar(key[i% keylength],message[i])
    return encoded.upper()

def vigenere_decryption(key,message):
    #getting rid of the spaces
    message.replace(" ","")
    decoded = ''
    keylength = len(key)
    for i in range(len(message)):
        decoded += decryptcaesar(key[i% keylength],message[i])
    return decoded.upper()