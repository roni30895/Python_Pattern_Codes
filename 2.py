def RAT(n):
    if n>1:
        # for i in range(0, n):
        #     for j in range(0, i+1):
        #         print("* ",end="")
        #     print("\r")
        for i in range(1,n+1):
            print("*" * i,(n-i) * " ")
    else:
             
        print("\n Please Enter the correct input.")
        print()
# Driver Code
n = int(input("\n Enter the number of rows : "))
RAT(n)
