def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

if __name__ == "__main__":
    a=35
    b=15
    print(gcd(a,b))
    