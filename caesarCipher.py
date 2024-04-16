try:
    import pyperclip # copies text  to the clipboard
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caeser Cipher')
print('The Caesar cipher encrpts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on')

while True: # keep asking until the user enters e or d
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    print('Please enter the letter e or d.')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key(0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}.'.format(mode))
message = input('> ')

# cipher only works with upper case letters
message = message.upper()

# stores e/d form of the message
translated = ''

# encryt/decrypt
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)  #get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num + len(SYMBOLS)
            num = num -key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass


