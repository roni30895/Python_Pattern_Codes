def Reverse_RAT(n):
    if n>1:
        for i in range(n):
            for j in range(n-i):
                print("* ",end="")
            print("\r")
    else:
             
        print("\n Please Enter the correct input")
        print()

# Driver Code
n = int(input("\n Enter the number of rows : "))
Reverse_RAT(n)
