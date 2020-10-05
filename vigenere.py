def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string)-len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
def ecncrypt(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
3
def decrypt(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
      
while(True):
    choice=(int(input("\n\nSelect:\n1.Encrypt\n2.Decrypt\n3.Exit\n:")))
    if(choice==1):
        string = str(input("Enter message:"))
        string=string.upper()
        key_ = str(input("Enter key:"))
        key = generateKey(string, key_) 
        en=ecncrypt(string,key) 
        print("Encrypted Text: {}".format(en))
    elif(choice==2):
        string = str(input("Enter encrypted message:"))
        key_ = str(input("Enter key:"))
        key = generateKey(string, key_)       
        dec=decrypt(string, key)
        print("Decrypted Text: {}".format(dec))
    elif(choice==3):
        exit(0)
    else:
        print("Invalid input!!!")