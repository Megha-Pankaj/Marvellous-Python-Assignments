def FTOC(C):
    F = C*(9/5)+32
    print("temperature in Farenheit",F)
    
    
def main():
    temp = int(input("Enter temprature in celcius"))
    FTOC(temp) 
                   
 
   
    
if __name__ == "__main__":
    main()