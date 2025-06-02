def Age_status(n):
    if n >= 18:
        print("You can vote")
    else:
        print("You cant vote")
        
def main():
    age = int(input("Enter your Age to check eligibility to vote:")) 
    Age_status(age)
    
if __name__ == "__main__":
    main()               