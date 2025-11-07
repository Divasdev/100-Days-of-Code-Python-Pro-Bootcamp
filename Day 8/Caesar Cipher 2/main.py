alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text,shift_amount):
    decrypted_text = ""
    for letter  in original_text:
      old_index= alphabet.index(letter)
      new_index = (old_index - shift_amount) % 26
      new_letter= alphabet[new_index]
      decrypted_text +=new_letter
    print(f"Decrypted text is {decrypted_text}")
def encrypt(original_text,shift_amount):
    encrypted_text = ""
    for letter  in original_text:
      old_index= alphabet.index(letter)
      new_index = (old_index + shift_amount) % 26
      new_letter= alphabet[new_index]
      encrypted_text +=new_letter
    print(f"Encrypted text is {  encrypted_text }")


def caeser(direction):
    if direction=='encode':
        encrypt("divas",5)
    else:
        decrypt("sharma",8)


caeser('encode')






