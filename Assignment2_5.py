def prime_ornot(no1):
    for i in range (2, no1-1):
        if no1 % i == 0:
            print("It is not a prime number")
            break
        else:
            print("It is a prime number")
            break
                
    
def main():
    no1 = int (input ("enter the number you want to check whether it is prime or not:"))
    prime_ornot(no1)
     


if __name__ == "__main__":
    main()    