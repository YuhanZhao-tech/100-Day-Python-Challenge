# Caesar cipher
import string

alphabet = list(string.ascii_lowercase)
option_dict = {"encode": "+", "decode": "-"}

def cipher(message, shift, option):

    encoded_message = ""
    for i in message.lower():
        
        #shift = eval(option_dict[option] + str(shift))
        index_before = alphabet.index(i)
        # "5+10"
        index_after = eval(str(index_before) + option_dict[option] + str(shift))
        if index_after > 25:
            index_after -= 26

        encoded_message += alphabet[index_after]
    
    return encoded_message

print(cipher("hello", 7, "encode"))