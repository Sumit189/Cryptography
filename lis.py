def lis(ar):
    temp=list(ar)
    seq=list()
    count=1
    for i in range(1,len(temp)):
        if(temp[i]>temp[i-1]):
            count+=1
            if(i==(len(temp)-1)):
                seq.append(count)
        else:
            seq.append(count)
            
    return max(seq)


arr = [41, 18467, 6334, 26500, 29169]
print(lis(arr))
