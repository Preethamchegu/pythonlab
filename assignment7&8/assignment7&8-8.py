Code = input("Enter the coded Message: ")
def decode_message(message, index=0, decoded=''):
    if index == len(message):
        print(decoded)
    if index < len(message) and 1 <= int(message[index]) <= 9:
        decode_message(message, index + 1, decoded + chr(64 + int(message[index])))
    if index + 1 < len(message) and 10 <= int(message[index:index+2]) <= 26:
        decode_message(message, index + 2, decoded + chr(64 + int(message[index:index+2])))

decode_message(Code)