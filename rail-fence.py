def enc(text, key):  
    arr = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
    down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
        if (row == 0) or (row == key - 1): 
            down = not down 
    
        arr[row][col] = text[i] 
        col += 1
          
        if down: 
            row += 1
        else: 
            row -= 1
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if arr[i][j] != '\n': 
                result.append(arr[i][j]) 
    return("" . join(result)) 
      
def dec(cipher, key): 
    arr = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    down = None
    row, col = 0, 0
       
    for i in range(len(cipher)): 
        if row == 0: 
            down = True
        if row == key - 1: 
            down = False
          
        arr[row][col] ='$'
        col += 1
          
        if down: 
            row += 1
        else: 
            row -= 1
              
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((arr[i][j] == '$') and
               (index < len(cipher))): 
                arr[i][j] = cipher[index] 
                index += 1
          
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        if row == 0: 
            down = True
        if row == key-1: 
            down = False
              
        if (arr[row][col]!='$'): 
            result.append(arr[row][col]) 
            col += 1
        
        if down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 
  
if __name__ == "__main__": 
    message="Hello there"
    key=3
    encrypt=enc(message,key)
    print("encrypted: "+encrypt)
    decrypt=dec(encrypt,key)
    print("decrypted: "+decrypt)