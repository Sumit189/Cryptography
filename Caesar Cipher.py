def encrypt(msg,key):
    res=""
    for i in range(len(msg)):
        C_upperLimit=ord('Z')
        s_upperLimit=ord('z')
        if(msg[i]==" "):
            res+="_"
        else:
            if(msg[i].isupper()):
                if(ord(msg[i])+key>C_upperLimit):
                    res+=chr((ord(msg[i])+key)-26)
                else:
                    res+=chr((ord(msg[i])+key))
            else:
                if(ord(msg[i])+key>s_upperLimit):
                    res+=chr((ord(msg[i])+key)-26)
                else:
                    res+=chr((ord(msg[i])+key))
    return res

def decrypt(msg,key):
    res=""
    for i in range(len(msg)):
        C_lowerLimit=ord('A')
        s_lowerLimit=ord('a')
        if(msg[i]=='_'):
            res+=" "
        else:
            if(msg[i].isupper()):
                if(ord(msg[i])-key<C_lowerLimit):
                    res+=chr((ord(msg[i])-key)+26)
                else:
                    res+=chr((ord(msg[i])-key))
            else:
                if(ord(msg[i])-key<s_lowerLimit):
                    res+=chr((ord(msg[i])-key)+26)
                else:
                    res+=chr((ord(msg[i])-key))
    return res


while(True):
    print("\nSelect:\n1.Encrypt\n2.Decrypt\n3.Exit\n:")
    choice=int(input())
    if choice==1:
        print("Enter msg to encrypt: ")
        msg=str(input())
        print("Enter Key: ")
        key=int(input())
        enc=encrypt(msg,key)
        print("Encrypted: {}".format(enc))
    elif choice==2:
        print("Enter msg to decrypt: ")
        enc=str(input())
        print("Enter Key: ")
        key=int(input())      
        dec=decrypt(enc,key)
        print("Decrypted: {}".format(dec))
    elif choice==3:
        exit(0)
    else:
        continue