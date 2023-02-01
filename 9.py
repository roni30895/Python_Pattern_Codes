def sq_pattern(n):
    if n>1:

        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()
    else:
        print("\n Please Enter the correct input.")
        print()

if __name__=="__main__":
    n = int(input("\n Enter the number of rows (Number should be more than 1) : "))
    sq_pattern(n)