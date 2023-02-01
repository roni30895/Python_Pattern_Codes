def half_triangle_right(n):
    if n>1:
        for i in range(0, n):
            for j in range(0, i+1):
                print("* ",end="")
            print("\r")
        for i in range (n,-1,-1):
            for j in range(i,-1,-1):
                print("* ",end="")
            print("\r")
    else:
        print("\n Please Enter the correct input.")
        print()
#Driver code

if __name__=="__main__":
    n = int(input("\n Enter the number of rows : "))
    half_triangle_right(n)
