import Arithmetic

def main():
    no1 = int(input("Enter First Number"))
    no2 = int(input("Enter Second Number"))
    print("Addition of two numbers is:",Arithmetic.Add(no1,no2))
    print("Substraction of two numbers is:",Arithmetic.Sub(no1,no2))
    print("Multiplication of two numbers is:",Arithmetic.Mult(no1,no2))
    print("Division of two numbers is:",Arithmetic.Div(no1,no2))
    
    
    
if __name__ == "__main__":
    main()    
    
    