def sum_fact_digits(no1):
    sum = 0
    for i in range (1, no1+1):
        sum = sum + i
    return sum 
    
def main():
    no1 = int (input ("enter the number you want to sum"))
    print("Addition of digits is:",sum_fact_digits(no1)) 


if __name__ == "__main__":
    main()    