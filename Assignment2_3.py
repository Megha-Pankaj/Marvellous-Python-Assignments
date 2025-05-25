def Fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact    



def main():
    n = int (input ("factorial you want to print"))
    print("factorial of given number is",Fact(n))
   

if __name__ == "__main__":
    main()