def ET(n):
    if n>1 and n%2!=0:
        # for i in range(n):
        #     for j in range(n-i-1):
        #         print(" ",end="")
        #     for k in range(2*i-1):
        #         print("*",end="")
        #     print()
        for j in range(1,n+1,2):
            print(" " * ((n-j)//2) + "*" * j + " " * ((n-j)//2))
    else:
             
        print("\n Please Enter the correct input.")
        print()
n = int(input("\n Enter the number of rows : "))
ET(n)
