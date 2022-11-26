n=int(input("ENTER NUMBER"))
if n==2:
    print('prime')
elif n==3:
    print('prime')
elif n>3:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print('not prime')
            break
    else:
        print('prime')
else:
    pass
