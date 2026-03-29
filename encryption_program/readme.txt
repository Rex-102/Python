#Encryption program
A basic command line program which converts user given input into encrypted format and again you can take the encrypted format then decrypts it.
## Features
- Encrypt any string including numbers, symbols and letters
- Decrypt encrypted text back to original
- Randomized substitution cipher for unique encryption each run

## Requirements
- Python 3.x
- No external dependencies

## How to Use
1. Run the script: python main.py
2. Enter the string you want to encrypt then decrypt
3. View your encrypted and decrypted Output

## Example Output
Enter the text you want to encrypt: I like to eat 
The original text is : I like to eat
The encrypted text is : [,L>gN,.#,N:.
Enter the text you want to decrypt: [,L>gN,.#,N:.
The encrypted text is : [,L>gN,.#,N:.
The decrypted text is : I like to eat

## Technologies Used
- random module
- string module

P.S. The encryption and decryption will be different when running the program again due to the random module selecting random equivalents of each character.