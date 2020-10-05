def encrypt_decrypt(msg,key):
    counter=0
    numeric_form=[]
    for j in range(len(msg)):
        counter=0
        for i in range(ord('A'),ord('Z')+1):
            if(i==ord(msg[j])):
                numeric_form.append(counter)
            counter+=1
    #key
    counter=0
    numeric_form_key=[]
    for j in range(len(key)):
        counter=0
        for i in range(ord('A'),ord('Z')+1):
            if(i==ord(key[j])):
                numeric_form_key.append(counter)
            counter+=1

    res=""
    for i in range(len(key)):
        res+=chr(((numeric_form[i]^numeric_form_key[i]))+65)
    return res


while(True):
    choice=int(input("\n\nPress:\n1. Encrypt\n2. Decrypt\n3. Exit\n"))
    if choice==1:
        msg=str(input("Enter Message: "))
        msg=msg.upper()
        key=str(input("Key: "))
        key=key.upper()
        en=encrypt_decrypt(msg,key)
        print("Encrypted msg: ",en)

