def Diamond(n):
    # k=2*n-2
    # for i in range(0,n): 
    #     for j in range(0,k):
    #         print(end=" ")
    #     k=k-1
    #     for j in range(0,i+1):
    #         print("*",end=" ")
    #     print("")
    
    # l=n-2 

    # for i in range(n,-1,-1):
    #     for j in range(l,0,-1):
    #         print(end=" ")
    #     l=l+1
    #     for j in range(0,i+1):
    #         print("*",end=" ")
    #     print("")
#########################################################

# Method 2

    if n>1 and n%2!=0:
    
        for i in range(1,n+1,2):
            print(" " * ((n-i)//2) + "*" * i + " " * ((n-i)//2))

        for j in range(n-2,0,-2):
            print(" " * ((n-j)//2) + "*" * j + " " * ((n-j)//2))
    
    else:
             
        print("\n Please Enter the correct input as odd number")
        print()
    

# Driver code
if __name__=="__main__":
    n = int(input("\n Enter the number of rows : "))
    Diamond(n)
