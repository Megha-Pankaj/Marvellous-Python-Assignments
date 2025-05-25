from MarvellousNum import check_primes_in_list 

def main():
    print("How many elements do you want:")
    size = int(input())
    Data =list()
    sum = 0
    
    print("Enter the values")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    list2 = check_primes_in_list(Data)
    
    for i in list2:
        sum = sum+i
    print(sum)  
    
if __name__ == "__main__":
    main()      
        