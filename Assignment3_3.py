def main():
    print("How many elements do you want:")
    size = int(input())
    Data =list()
    min = 0
    
    
    print("Enter the values")
    for i in range(size):
        no = int(input())
        Data.append(no)
        
    min=Data[0]
    for n in range(0,len(Data)):
        if Data[n]<=min:
            min=Data[n]
    print("Minimum element from the list is:",min)          
        

        
if __name__ == "__main__":
    main()