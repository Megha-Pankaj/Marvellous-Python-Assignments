def main():
    print("How many elements do you want:")
    size = int(input())
    Data =list()
    max = 0
    
    
    print("Enter the values")
    for i in range(size):
        no = int(input())
        Data.append(no)
        
    max=Data[0]
    for n in range(0,len(Data)):
        if Data[n]>=max:
            max=Data[n]
    print("Maximum element from the list is:",max)          
        

        
if __name__ == "__main__":
    main()