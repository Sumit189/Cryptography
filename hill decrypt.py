import numpy as np
from sympy import Matrix
import math

np.keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]
plainMatrix = [[0] for i in range(3)]
np.inverseKeyMatrix = [[0] * 3 for i in range(3)]

def makeKeyMatrix(key):
  k = 0
  for i in range(3):
    for j in range(3):
      np.keyMatrix[i][j] = ord(key[k]) % 65
      k += 1

def makeInverseKeyMatrix(key):
    makeKeyMatrix(key)
    keyMatrix=np.keyMatrix
    inverseKeyMatrix = Matrix(keyMatrix).inv_mod(26)
    np.inverseKeyMatrix = np.array(inverseKeyMatrix)

def decrypt(message,key):
    makeInverseKeyMatrix(key)
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    for i in range(3):
        for j in range(1):
            plainMatrix[i][j] = 0
        for x in range(3):
            plainMatrix[i][j] = plainMatrix[i][j] % 26
            plainMatrix[i][j] += (np.inverseKeyMatrix[i][x] * messageVector[x][j])
        plainMatrix[i][j] = plainMatrix[i][j] % 26
        PlainText = []
    for i in range(3):
        PlainText.append(chr(int(round(plainMatrix[i][0]) + 65)))
    return ("".join(PlainText))

message = input("Enter Message:")
message = message.upper()
message = message.replace(" ","")
key = input("Key:")
key = key.upper()
dec=decrypt(message,key)
print("Decrypted: ",dec)