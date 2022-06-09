#basic encryption project

keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(26):
    x = input("What do you want the key for " + alphabet[i] + " to be?")
    keys[i] = x

print(keys)