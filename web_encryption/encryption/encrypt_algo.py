import random
import string
custom_word_dict = {}

custom_word_dict['RG43s']="##randomstring1##"
custom_word_dict['Heart Sender']="##randomstring2##"
custom_word_dict['Mkato']="##randomstring3##"
custom_word_dict['Random language']="##randomstring4##"

def encrypt_text(text,custom_word):
    result_str=''
    for _ in text:
        result_str += str(_) + "<span style='color:transparent;font-size: 0%;'>"+ custom_word_dict[custom_word]+ "</span>"  
    print(result_str) 
    return result_str