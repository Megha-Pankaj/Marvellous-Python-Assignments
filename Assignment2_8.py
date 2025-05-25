def Nums(rows):
   for i in range(1,rows+2):
    for j in range(1,i):
        print(j, end=' ')
    print('')
    

def main():
    no1 = int (input ("How many num you want to print"))
    Ans = Nums(no1)
    return Ans

if __name__ == "__main__":
    main()