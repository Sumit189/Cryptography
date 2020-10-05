import math
def encrypt(message,key,pattern):
    row=math.ceil(len(message)/len(key))
    arr=[[0 for i in range(len(key))] for j in range(row)]
    k=0
    for i in range(0,row):
        for j in range(0,len(key)):
            if (k>=len(message)):
                arr[i][pattern[j]]="x"
            else:
                arr[i][pattern[j]]=message[k]
            k+=1
                
    res=""
    for i in range(len(key)):
            for j in range(row):
                if arr[j][i]!=0:
                    res+=arr[j][i]
    return res

def decrypt(message,key,pattern):
    row=math.ceil(len(message)/len(key))
    arr=[[0 for i in range(len(key))] for j in range(row)]
    k=0
    for i in range(len(key)):
        for j in range(row):
            if k>=len(message):
                arr[j][i]=""
            else:
                arr[j][i]=message[k]
            k+=1
    
    res=""
    for i in range(row):
        for j in range(len(key)):
            res+=arr[i][pattern[j]]
    
    return res

def make_pattern(duplicate_key,sorted_key):
    op=0
    for i in range(len(duplicate_key)):
        index=duplicate_key.index(sorted_key[i])
        duplicate_key[index]=op
        op+=1
    return duplicate_key



while(True):
    choice=(int(input("\n\nSelect:\n1.Encrypt\n2.Decrypt\n3.Exit\n:")))
    if(choice==1):
        message=input("Enter Message: ")
        key=input("Enter Encryption Key: ")
        key=key.lower()
        sorted_key=[char for char in key]
        sorted_key.sort()
        duplicate_key=[char for char in key]
        pattern=make_pattern(duplicate_key,sorted_key)
        en=encrypt(message,key,pattern)
        print("Encrypted Text: {}".format(en))
    elif(choice==2):
        message=input("Enter Encrypted Message: ")
        key=input("Enter Decryption Key: ")
        key=key.lower()
        sorted_key=[char for char in key]
        sorted_key.sort()
        duplicate_key=[char for char in key]
        pattern=make_pattern(duplicate_key,sorted_key)       
        dec=decrypt(message,key,pattern)
        print("Decrypted Text: {}".format(dec))
    elif(choice==3):
        exit(0)
    else:
        print("Invalid input!!!")


