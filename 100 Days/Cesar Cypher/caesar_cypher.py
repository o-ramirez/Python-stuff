from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

  

def caesar(text, shift, direction):

  cipher_list = []
  if direction == "encode":
    for n in text:
      if n not in alphabet:
            cipher_list += str(n)
      else:
        iCheck = alphabet.index(n)
        cCheck = iCheck + shift
        if cCheck > 25:
          shift = shift % 26
          cCheck = 0 + shift - 1  
        cipher_list += alphabet[cCheck]
        cipher_text = ""
    print(f'The encoded text is {cipher_text.join(cipher_list)}')

  elif direction == "decode":
    for n in text:
      if n not in alphabet:
            cipher_list += str(n)
      else:
        iCheck = alphabet.index(n)
        cCheck = iCheck - shift
        
        if cCheck < 0:
          shift = shift % 26
          cCheck = 25 - shift + 1  
        cipher_list += alphabet[cCheck]
        cipher_text = ""
    print(f'The decoded text is {cipher_text.join(cipher_list)}') 



#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
keep_going = True

while keep_going == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text = text, shift = shift, direction = direction)
  restart = input(f'Type yes if you wish to encode or decode again. Otherwise type no to quit. ' )
  if restart == "yes":
    continue
  else:
    keep_going = False
  
