def Add(no1,no2):
    ans = no1+no2
    return ans

def Sub(no1,no2):
    ans = no1-no2
    return ans

def Mult(no1,no2):
    ans = no1*no2
    return ans

def Div(no1,no2):
    ans = no1/no2
    return ans


def main():
    no1 = int(input("Enter first Number"))
    no2 = int(input("Entr second Number"))
    print("Sum:",Add(no1,no2))
    print("Difference:",Sub(no1,no2))
    print("Product:",Mult(no1,no2))
    print("Division:",Div(no1,no2))   
    

if __name__ == "__main__":
    main()
 