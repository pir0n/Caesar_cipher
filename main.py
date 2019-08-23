# Kuba_Gryglak_@2019

def_num = input("To encrypt press 1 \n"
                "To decrypt press 2 \n"
                "To crack press 3 \n")

def encryption():
    message_encrypted = ""
    message_to_encrypt = input("Enter the message to encrypt.")
    num = int(input("Enter the number of positions to move"))
    for i in range(len(message_to_encrypt)):
        sign = chr((ord(message_to_encrypt[i])+num))
        message_encrypted = message_encrypted + sign
    print(message_encrypted)

    # def decrypt():
    #     message_to_decrypt = input("Enter the message to decrypt.")
    #     num = input("Enter the number of positions to move")
    #     for i in len(message_to_decrypt):
    #         message_to_decrypt[i] = (int(message_to_decrypt) + num) % 25
    #     print(message_to_decrypt)
    #
    # def crack():
    #     message_to_crack = input("Enter the message to crack.")
    #     num = input("Enter the number of positions to move")
    #     for i in len(message_to_crack):
    #         message_to_crack[i] = (int(message_to_crack) + num)%25
    #     print(message_to_crack)

if def_num == '1':
    encryption()
# elif def_num == 2:
#     decrypt()
# elif def_num == 3:
#     crack()