def Stars(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()



def main():
    no1 = int (input ("How many stars you want to print"))
    Ans = Stars(no1)
    return Ans

if __name__ == "__main__":
    main()
    