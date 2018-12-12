"""A collection of cuntions for encryptions"""
import string

# This is the module for the encyptions



# key encryption from the class
def key_encryption(key,message):
    ''' Receive a messgae and a key, using the key 
        to encoded the message
    Parameters: 
    -----------
    key: int
        The key use to encrypt the message
    message: str
        The message to encrypt
        
    return:
        str
    '''
    encoded = ''
    #for every char in the message, use ord to get the 
    # unicode for the char, add the key and convert it 
    #bcak to char
    for char in message:
        encoded = encoded +  chr(ord(char) + key)
    return encoded

# decrption function for the key encryption 
def key_decryption(key,message):
    ''' Receive a messgae and a key, using the key 
        to decrypt the message
    Parameters: 
    -----------
    key: int
        The key use to decrypt the message
    message: str
        The message to decrypt
    return:
        str
    '''
    decoded = ''
    #for every char in the message, use ord to get the 
    # unicode for the char, subtract the key and convert it 
    #bcak to char
    for char in message:
        decoded = decoded +  chr(ord(char) - key)
    return decoded


# caesar encryption 
def encryptcaesar(key,message):
    ''' Receive a messgae and a key, using the key 
        to encode the message
    Parameters: 
    -----------
    key: str
        The key use to encrypt the message
    message: str
        The message to encrypt
    return:
        str
    '''    
    message = str(message).upper()
    key=str(key)
    #add the key to every alphabet of the string and convert it back to
    #alphabet
   
    encoded = ''.join([chr(97 + (ord(i) + ord(key.upper()))% 26) for i in message])
    return encoded

def decryptcaesar(key,message):
    ''' Receive a messgae and a key, using the key 
        to encoded the message
    Parameters: 
    -----------
    key: int
        The key use to decrypt the message
    message: str
        The message to decrypt
    return:
        str
    '''
    message = str(message).upper()
    key = str(key)
    decoded = ''.join([chr(97 + (ord(i) - ord(key.upper()))% 26)  for i in message])
    return decoded

def vigenere_encryption(key,message):
    ''' Receive a messgae and a key, using the key 
        to encode the message
    Parameters: 
    -----------
    key: str
        The key use to encrypt the message
    message: str
        The message to encrypt
    return:
        str
    '''        
    #getting rid of the spaces
    message=message.replace(" ","")
    encoded = ''
    keylength = len(key)
    # keey shifting the character in the string with the given key
    for i in range(len(message)):
        encoded += encryptcaesar(key[i% keylength],message[i])
    return encoded.upper()

def vigenere_decryption(key,message):
    ''' Receive a messgae and a key, using the key 
        to decrypt the message
    Parameters: 
    -----------
    key: str
        The key use to decrypt the message
    message: str
        The message to decrypt
    return:
        str
    '''    
    #getting rid of the spaces
    message=message.replace(" ","")
    decoded = ''
    keylength = len(key)
    # keep shifting the character back to its original character
    for i in range(len(message)):
        decoded += decryptcaesar(key[i% keylength],message[i])
    return decoded.upper()