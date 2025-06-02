def Calculate_Area_Perimeter(l,w):
    Area = l*w
    Perimeter = 2*(l+w)
    print("Area:",Area)
    print("Perimeter:",Perimeter)




def main():
    no1 = int(input("Enter length"))
    no2 = int(input("Enter width"))
    Calculate_Area_Perimeter(no1,no2)
      
    

if __name__ == "__main__":
    main()