# Hash Function
def hash(input_char):

    ascii_check = ord(input_char)

    # If Uppercase
    if ascii_check >= 65 and ascii_check <= 90:
        
        # Return Hash Value
        return ascii_check - 65

    # If Lowercase
    if ascii_check >= 97 and ascii_check <= 122:
        
        # Return Hash Value
        return ascii_check - 97


