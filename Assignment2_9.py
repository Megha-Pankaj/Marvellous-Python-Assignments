
def Digit_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    print(count)    
    

def main():
    no1 = int (input ("How many num you want to print"))
    Ans = Digit_count(no1)
    return Ans

if __name__ == "__main__":
    main()