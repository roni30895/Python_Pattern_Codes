def x_pattern(n):
    if n>1 and n%2!=0:
    
        for i in range(n,1,-2):
            print(" " * ((n-i)//2) + "*" * i + " " * ((n-i)//2))

        for j in range(1,n+1,2):
            print(" " * ((n-j)//2) + "*" * j + " " * ((n-j)//2))
    else:
        print("\n Please Enter the correct input as odd number")
        print()

if __name__=="__main__":
    n = int(input("\n Enter the odd number of rows : "))
    x_pattern(n)