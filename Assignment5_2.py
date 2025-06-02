def vowel_check(x):
    if(x =='a' or x =='e'or x =='i' or x =='o' or x =='u' ):
        print("Vowel")
    else:
        print("Consonenant")    



def main():
    alpha =input("Enter Aplhabet to check")
    vowel_check(alpha)  
    

if __name__ == "__main__":
    main()