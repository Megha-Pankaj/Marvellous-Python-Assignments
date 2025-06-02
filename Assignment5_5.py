def even_odd_number(num):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")   
        
        
def main():
    no1 = int(input("Enter  number"))
    even_odd_number(no1)
 
   
    
if __name__ == "__main__":
    main()      