n = int(input("Enter your age:"))

if(n>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(n<0):
    print("You are entering invalid negative age")

elif(n==0):
    print("You are entering 0 which is not a valid age")
    
else:
    print("You are below the age of consent")