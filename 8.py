def half_triangle_left(n):
    if n>1:
    
        for i in range(1, n+1):
            print(" " * (n- i) + "*" * i)
    
        for j in range(n-1,0,-1):
            print(" " * (n-j) + "*" * j)
    else:
        print("\n Please Enter the correct input.")
        print()
  
if __name__=="__main__":
    n = int(input("\n Enter the number of rows : "))
    half_triangle_left(n)
