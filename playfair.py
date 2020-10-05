def encrypt(msg,matrix):             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]

    if len(msg)%2!=0:
        msg=msg[:]+'X'

    res=""
    while i<len(msg):
        loc=list()
        loc=find_index(msg[i])
        loc1=list()
        loc1=find_index(msg[i+1])
        if loc[1]==loc1[1]:
            res+=("{}{}".format(matrix[(loc[0]+1)%5][loc[1]],matrix[(loc1[0]+1)%5][loc1[1]]))
        elif loc[0]==loc1[0]:
            res+=("{}{}".format(matrix[loc[0]][(loc[1]+1)%5],matrix[loc1[0]][(loc1[1]+1)%5]))  
        else:
            res+=("{}{}".format(matrix[loc[0]][loc1[1]],matrix[loc1[0]][loc[1]]))    
        i=i+2   
    return res     
                 
def decrypt(msg,matrix):
    i=0
    res=""
    while i<len(msg):
        loc0=list()
        loc0=find_index(msg[i])
        loc1=list()
        loc1=find_index(msg[i+1])
        if loc0[1]==loc1[1]:
            res+=("{}{}".format(matrix[(loc0[0]-1)%5][loc0[1]],matrix[(loc1[0]-1)%5][loc1[1]]))
        elif loc0[0]==loc1[0]:
            res+=("{}{}".format(matrix[loc0[0]][(loc0[1]-1)%5],matrix[loc1[0]][(loc1[1]-1)%5]))  
        else:
            res+=("{}{}".format(matrix[loc0[0]][loc1[1]],matrix[loc1[0]][loc0[1]]))    
        i=i+2  
    return res

def find_index(c): 
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc

def fill(key,msg):
    filled=list()
    for i in range(len(key)):
        if key[i] not in filled:
            if key[i]=='J':
                filled.append('I')
            else:
                filled.append(key[i])
    for c in key:
        if c not in filled:
            if c=='J':
                filled.append('I')
            else:
                filled.append(c)
    flag=0
    for i in range(65,91): 
        if chr(i) not in filled:
            if i==73 and chr(74) not in filled:
                filled.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                filled.append(chr(i))
    return filled

while(True):
    choice=(int(input("\n\nSelect:\n1.Encrypt\n2.Decrypt\n3.Exit\n:")))
    if(choice==1):
        msg=input("Enter Message: ")
        key=input("Enter Key: ")
        msg=msg.upper().replace(" ","")
        key=key.upper().replace(" ","")
        matrix=[[0 for x in range(5)] for y in range(5)]
        filled=fill(key,msg)
        k=0
        for i in range(0,5):
            for j in range(0,5):
                matrix[i][j]=filled[k]
                k+=1
        en=encrypt(msg,matrix)
        print("Encrypted msg: {}".format(en))
    elif(choice==2):
        msg=input("Enter Encrypted Message: ")
        key=input("Enter Key: ")
        msg=msg.upper().replace(" ","")
        key=key.upper().replace(" ","")   
        matrix=[[0 for x in range(5)] for y in range(5)]    
        filled=fill(key,msg)
        k=0
        for i in range(0,5):
            for j in range(0,5):
                matrix[i][j]=filled[k]
                k+=1
        de=decrypt(msg,matrix)
        print("Decrypted msg: {}".format(de))
    elif(choice==3):
        exit(0)
    else:
        print("Invalid input!!!")