n1=int(input("ENTER LOWER LIMIT"))
n2=int(input("ENTER UPPER LIMIT"))
for i in range(n1,n2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
