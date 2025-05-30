def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)


def main():
    num = int(input("Enter the number to print its factorial:"))
    factorial(num)
        
if __name__ == "__main__":
    main() 