from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo+"\n")


# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         shift_index = alphabet.index(letter) + shift_amount
#         # if shift_index > 25 :
#         #     shift_index = shift_index - len(alphabet)
#         shift_index %= len(alphabet)  # z -> 26 % len() -> 26 = 0, 35 % len() -> 26 = 9
#         encrypted_text += alphabet[shift_index]
#     print(f"Here is the encoded result: {encrypted_text}")
#
#
# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for letter in original_text:
#         shift_index = alphabet.index(letter) - shift_amount
#         # if shift_index < 0 :
#         #     shift_index = shift_index + len(alphabet)
#         shift_index %= len(alphabet)  # a -> -1 % len() -> 26 = 25
#         decrypted_text += alphabet[shift_index]
#     print(f"Here is the decoded result: {decrypted_text}")


# encrypt(text, shift)
# decrypt(text,shift)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    unused_char = ""
    if encode_or_decode == "decode":
        shift_amount *= -1  # this will turn the decoded amount to it's reverse if +ve no issue and it will substract instead +
                            # but this should run only for first char
    for letter in original_text:
        if letter in alphabet:
            shift_index = alphabet.index(letter) + shift_amount
            shift_index %= len(alphabet)
            output_text += alphabet[shift_index]
        else:
            unused_char += letter
    output_text += unused_char
    print(f"Here is the {encode_or_decode}d result: {output_text}")

continue_action = True
while continue_action :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, encode_or_decode=direction)
    action = input("Type 'yes' if you want to go again\nOtherwise, type 'no'.").lower()
    if action == "yes":
        continue_action = True
    else:
        continue_action = False