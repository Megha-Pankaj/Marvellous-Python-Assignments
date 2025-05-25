def Nums(rows):
    for i in range(1, rows+1):
        for j in range(1,rows+1):
            print("*", end=" ")
        print()



def main():
    no1 = int (input ("How many stars you want to print"))
    Ans = Nums(no1)
    return Ans

if __name__ == "__main__":
    main()