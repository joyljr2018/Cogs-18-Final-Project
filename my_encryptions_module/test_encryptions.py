import encryptions as en

# Tests for key_encryption function
# Create a key,message to test encrypt and decrypt functions
def test_key_encryptions():
    #Case 1
    key = 200
    message = 'Hello World'
    #run the key_encryption function and assign the result to encoded
    encoded = en.key_encryption(key,message)
    #decode the encoeded message and assign the result to decoded
    decoded = en.key_decryption(key,encoded)

    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    print("Testing for case 1 of key_encryption")
    assert encoded == 'ĐĭĴĴķèğķĺĴĬ'

    #Test if the encoded message decrypted correctly
    assert decoded == 'Hello World'
    print("Case 1 for key encryption passed ")

    #Case 2

    key = 100
    message = 'Cogs is the best'

    #run the key_encryption function and assign the result to encoded
    encoded = en.key_encryption(key,message)

    #decode the encoeded message and assign the result to decoded
    decoded = en.key_decryption(key,encoded)

    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    print("Testing for case 2 of key_encryption")
    assert encoded == '§ÓË×Í×ØÌÉÆÉ×Ø'

    #Test if the encoded message decrypted correctly
    assert decoded == 'Cogs is the best'
    print("Case 2 for key encryption passed ")
    #Case 3

    key = 300
    message = 'Cogs18 is the best'
    #run the key_encryption function and assign the result to encoded
    encoded = en.key_encryption(key,message)
    #decode the encoeded message and assign the result to decoded
    decoded = en.key_decryption(key,encoded)
    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)
    #Test if the message encrypted correctly
    print("Testing for case 3 of key_encryption")
    assert encoded == 'ůƛƓƟŝŤŌƕƟŌƠƔƑŌƎƑƟƠ'
    #Test if the encoded message decrypted correctly
    assert decoded == 'Cogs18 is the best'

    print("Case 3 for key encryption passed ")



# Tests for the simple Caesar encryptions
#create a key,message to test encrypt and decrypt functions
def test_caesar_encryption():
    
    #Case 1
    key = 'H'
    message = 'goodwork'
    #run the Caesar encryption function and assign the result to encoded
    encoded = en.encryptcaesar(key,message)
    #decode the encoeded message and assign the result to decoded
    decoded = en.decryptcaesar(key,encoded)
    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)
    #Test if the message encrypted correctly
    print("Testing for case 1 of encryptcaesar")
    assert encoded == 'nvvkdvyr'
    #Test if the encoded message decrypted correctly
    assert decoded == 'goodwork'

    print("Case 1 for caesar encryption passed ")

    #Case 2
    key = 'b'
    message = 'goodmorning'

    #run the Caesar encryption function and assign the result to encoded
    encoded = en.encryptcaesar(key,message)

    #decode the encoeded message and assign the result to decoded
    decoded = en.decryptcaesar(key,encoded)

    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    print("Testing for case 2 of encryptcaesar")
    assert encoded == 'hppenpsojoh'
    #Test if the encoded message decrypted correctly
    assert decoded == 'goodmorning'

    print("Case 2 for caesar encryption passed ")

    #Case 3
    key = 'K'
    message = 'seeyoutomorrow'

    #run the Caesar encryption function and assign the result to encoded
    encoded = en.encryptcaesar(key,message)

    #decode the encoeded message and assign the result to decoded
    decoded = en.decryptcaesar(key,encoded)

    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    print("Testing for case 3 of encryptcaesar")
    assert encoded == 'cooiyedywybbyg'

    #Test if the encoded message decrypted correctly
    assert decoded == 'seeyoutomorrow'

    print("Case 3 for caesar encryption passed ")

    
    
#Tests for vigenere_encryption functions 
#create a key,message to test encrypt and decrypt functions
def test_vigenere_encryption():
    #Case 1
    key = 'APPLE'
    message = "Today is a rainy day"
    #run the Vigenere encryption function and assign the result to encoded


    encoded = en.vigenere_encryption(key,message)
    #decode the encoeded message and assign the result to decoded

    decoded = en.vigenere_decryption(key,encoded)

    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    print("Testing for case 1 of Vigenere_encryption")
    assert encoded == "TDSLCIHPCEICNOEY"

    #Test if the encoded message decrypted correctly
    assert decoded == 'TODAYISARAINYDAY'

    print("Case 1 for vigenere encryption passed ")

    #Case 2
    key = 'BANANA'
    message =  "Tomorrow is a better day! "

    #run the Caesar encryption function and assign the result to encoded
    print("Testing for case 2 of Vigenere_encryption")
    encoded = en.vigenere_encryption(key,message)
    #decode the encoeded message and assign the result to decoded
    decoded = en.vigenere_decryption(key,encoded)


    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    assert encoded == 'UOZOERPWVSNBFTGEEDBYH'

    #Test if the encoded message decrypted correctly
    assert decoded == 'TOMORROWISABETTERDAYU'

    print("Case 2 for vigenere encryption passed ")

    #Case 3
    key = 'KIRLAND'
    message = "Purified water"

    #run the Caesar encryption function and assign the result to encoded
    encoded = en.vigenere_encryption(key,message)

    #decode the encoeded message and assign the result to decoded
    decoded = en.vigenere_decryption(key,encoded)


    #Test if they are returned as string
    assert isinstance(encoded, str)
    assert isinstance(decoded, str)

    #Test if the message encrypted correctly
    print("Testing for case 1 of Vigenere_encryption")
    assert encoded == 'ZCITFVHNEREEE'

    #Test if the encoded message decrypted correctly
    assert decoded == 'PURIFIEDWATER'

    print("Case 3 for vigenere encryption passed ")


    print("All the tests passed! good work!")
