def cutadd(text,m,n):
    t = list(text)
    temp = list(t)
    a=2
    count=0
    l= len(temp)
    for i in range(20):
        if a%2==0:
            temp=t[l-m:]+t[:l-m]
        else:
            temp=t[l-n:]+t[:l-n]
        count+=1
        a+=1
        t=temp
        # print(temp)/
        if(temp==list(text)):
            return (count)

print(cutadd("AbcDef",1,2))
ab=['a','b','c','d','e','f']
l=len(ab)
# print(ab[l-1:]+ab[:l-1])