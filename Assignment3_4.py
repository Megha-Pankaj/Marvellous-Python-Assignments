def main():
    print("How many elements do you want:")
    size = int(input())
    Data =list()
    min = 0
    
    
    print("Enter the values")
    for i in range(size):
        no = int(input())
        Data.append(no)
        
    element_to_check = int(input("Enter the number you need to check freqeuncy"))
    frequency = Data.count(element_to_check)
    print(f"The element {element_to_check} appears {frequency} times in the list.")
             
        

        
if __name__ == "__main__":
    main()




