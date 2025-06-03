def Square(x):
    result = lambda x : x ** 2
    return result(x)

def main():
    n=int(input("Enter your number:"))
    ans = Square(n)
    print("square of number is:",ans)
    
    
if __name__ == "__main__":
    main()