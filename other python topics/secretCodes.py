import random
import string


random_chars = ''.join(random.choices(string.ascii_letters, k=3))
modified_string = []

# print(random_chars)
def encode_string(string_to_encode):
    # print(string_to_encode)
    encoded_list_string=string_to_encode.split(" ")
    for i in range(0,len(encoded_list_string)):
        if(len(encoded_list_string[i])<3):
            two_letter_string_to_replace=encoded_list_string[i]
            two_letter_string=encoded_list_string[i][::-1] # reverse the string
            
            # replace the string with the reversed string
            replaced_str=encoded_list_string[i].replace(two_letter_string_to_replace,two_letter_string) 
       
        # add random characters to the string
        modified_string.append(replaced_str if len(encoded_list_string[i])<3 else random_chars+encoded_list_string[i]+random_chars) 
        
    return " ".join(modified_string)


string_to_encode="Hello World! Today is a good day"
encoded_string=encode_string(string_to_encode)
print(encoded_string)