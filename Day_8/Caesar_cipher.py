# Caesar cipher
import string

alphabet = list(string.ascii_lowercase)

def encode(message, shift):

    encoded_message = ""
    for i in message:
        
        index_before = alphabet.index(i)
        index_after = index_before + shift
        if index_after > 25:
            index_after -= 26

        encoded_message += alphabet[index_after]
    
    return encoded_message

def decode(message, shift):
    decoded_message = ""
    for i in message:
        
        index_before = alphabet.index(i)
        index_after = index_before - shift
        
        decoded_message += alphabet[index_after]
    
    return decoded_message
