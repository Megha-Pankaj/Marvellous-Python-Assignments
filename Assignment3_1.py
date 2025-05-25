def main():
    print("How many elements do you want:")
    size = int(input())
    Data =list()
    add_list = 0
    
    print("Enter the values")
    for i in range(size):
        no = int(input())
        Data.append(no)
        
    
    for value in Data:
        add_list = add_list + value 
    print(add_list)
    
            
    
if __name__ == "__main__":
    main() 