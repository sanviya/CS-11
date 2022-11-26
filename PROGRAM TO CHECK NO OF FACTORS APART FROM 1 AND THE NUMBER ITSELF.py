n=int(input("ENTER NUMBER"))
c=0
for i in range(2,(n//2)+1):
    if n%i==0:
        c+=1
print('Number of factors apart from 1 and the number itself=',c)

