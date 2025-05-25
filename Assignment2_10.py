
def Digit_Sum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    print(sum)     
    

def main():
    no1 = int (input ("How many num you want to print"))
    Ans = Digit_Sum(no1)
    return Ans

if __name__ == "__main__":
    main()