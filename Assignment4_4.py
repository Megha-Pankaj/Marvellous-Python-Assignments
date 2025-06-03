from functools import reduce

compare = lambda A: A%2 ==0

Increase = lambda A: A**2

Mult = lambda A,B :A + B

def main():
    data = []
    no1 = int(input("Enter the count:"))
    
    print("Enter the numbers from the list:")
    for i in range(no1):
        num = int(input())
        data.append(num)
    print("Input Data:",data) 
    
    FData = list(filter(compare,data))
    print("filter Data:",FData)
    
    
    Mdata = list(map(Increase,data))
    print("Map Data:",Mdata)
    
    
    Rdata = reduce(Mult,Mdata)
    print("Reduce output:",Rdata)
    
    
if __name__ == "__main__":
    main()  