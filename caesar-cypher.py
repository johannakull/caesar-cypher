alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  cypher_text = ""

  for letter in text:
    original_position = alphabet.index(letter)
    new_position = original_position + shift
    cypher_text += alphabet[new_position]

  print(f"The encoded text is {cypher_text}")

encrypt(text, shift)