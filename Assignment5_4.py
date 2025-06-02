def largest_numbers(no1,no2,no3):
    if no1 > no2 and no1 > no3 :
        print(f"{no1} is the largest number")
    elif no2 > no1  and no2 > no3:
        print(f"{no2} is the largest number") 
    else:
        print(f"{no3} is the largest number")





def main():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number")) 
    num3 = int(input("Enter Third number"))  
    largest_numbers(num1,num2,num3)
    
if __name__ == "__main__":
    main()