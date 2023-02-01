def Rev_ET(n):
    if n>1 and n%2!=0:
    #     for i in range(n,-1,-2): 
    #         for j in range(n,0,-1):
    #             print(" ",end=" ")
    #         n=n+1
    #         for k in range(0,i+1):
    #             print("*",end=" ")
    #         print()
        for i in range(n,0,-2):
            print(" " * ((n-i)//2) + "*" * i + " " * ((n-i)//2))    
    else:
             
        print("\n Please Enter the correct input as odd number")
        print()
n = int(input("\n Enter the number of rows : "))
Rev_ET(n)
