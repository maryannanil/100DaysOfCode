a=int(input("Enter num 1:"))
b=int(input("Enter num 2:"))
c=int(input("Enter num 3:"))
if a > b and a > c :
    print(a,"is greatest number")
elif b> a and b> c  :
    print(b, "is greatest number")
elif c>a and c> b: 
    print(c,"is greatest number")
elif b==a or b==c or a==c:
    print("Highest Number are same")
elif a==b==c:
    print("All 3 are same")
else:
    print("Invalid")
