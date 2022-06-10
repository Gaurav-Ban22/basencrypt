#basic encryption project

keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n", "o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(26):
    x = input("What do you want the key for " + alphabet[i] + " to be?")
    keys[i] = x

def loopMain():   
    ask = input("To encrypt a message write E. To check ur key write K.")
    if ask == "E":
        msg = input("Write your message: ")
        chars = list(msg)
        enc = ""
        for char in chars:
            cap = char
            if char in alphabet:
                num = alphabet.index(char)
                enc += keys[num] + " "
            elif char in lowalphabet:
                num = lowalphabet.index(char)
                enc += keys[num] + " "
            else:
                enc += char + " "
        
        print(enc)
    elif ask == "K":
        for i in range(26):
            print(alphabet[i] + ": " + keys[i])
    else:
        loopMain()   

while True:
    loopMain()


