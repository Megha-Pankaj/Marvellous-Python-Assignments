def prime_not(num):
    flag = False

    if num == 0 or num == 1:
        print(num, "is not a prime number")
    elif num > 1:
    
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
            break

    
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
               


def main():
    num = int(input("Enter the number :"))
    prime_not(num)
        
if __name__ == "__main__":
    main() 