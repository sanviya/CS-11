s=0
n1=int(input("ENTER DIGIT"))
n2=int(input("ENTER DIGIT"))
if n1>n2:
    for i in range(n2,n1+1):
        s+=i
    print(s)
elif n2>n1:
    for i in range(n1,n2+1):
        s+=i
    print(s)
else:
    print(s)

