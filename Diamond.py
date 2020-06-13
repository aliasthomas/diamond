"""Python code to make diamond pattern
   It is with two functions """

#function for first half
def up_triangle_base(n):
    for i in range(0,n+1):
        print(" " * (n-i) + "* " * i) #space give between quote is important
        
#function for second half
def down_triangle_base(n):
    for i in range(n-1,0,-1): #use for invert the above code
        print(" " * (n-i) + "* " * i)#space give between quote is important
        
up_triangle_base(5)
down_triangle_base(5)
