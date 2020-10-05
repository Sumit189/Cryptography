def extendedgcd(a,b):
    if a==0:
        return b,0,1
    gcd,x1,y1=extendedgcd(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    return gcd,x,y

if __name__ == "__main__":
    a=int(input("Enter 1st num: "))
    b=int(input("Enter 2nd num: "))
    g,x,y=extendedgcd(a,b)
    print("gcd={} x={} y={}".format(g,x,y))