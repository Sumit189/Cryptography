import numpy as np
np.keyMatrix = [[0] * 3 for i in range(3)]

def makeKeyMatrix(key):
  k = 0
  for i in range(3):
    for j in range(3):
      np.keyMatrix[i][j] = ord(key[k])%65
      k += 1

def encrypt(msg,key):
    makeKeyMatrix(key) 
    key=np.keyMatrix
    c=int(len(msg)/len(key[0]))
    r=int(len(msg)/c)
    char_matrix=[[0 for i in range(c)] for j in range(r)]
    result=[[0 for i in range(c)] for j in range(r)]
    k=0
    for i in range(0,len(char_matrix)):
        for j in range(0,len(char_matrix[0])):
            char_matrix[i][j]=(ord(msg[k])-65)
            k+=1

    for i in range(3): 
        for j in range(1): 
            for x in range(3): 
                result[i][j] += (key[i][x] * char_matrix[x][j]) 
            result[i][j]= result[i][j]%26
    
    res_char=""
    for i in range(len(result)):
        for j in range(len(result[0])):
            res_char+=chr((result[i][j]+65))
    return res_char

msg=input('Enter Message: ')
msg=msg.upper()
msg=msg.replace(" ","")
key = input("Key:")
key = key.upper()
en=encrypt(msg,key)
print("Encrypted: ",en)