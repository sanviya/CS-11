print("****MENU****")
print("1.Sum of digits")
print("2.Check Prime")
print("3.Count Vowels")
print("4.Exit") 
while True:
    ch=int(input("Enter the choice:"))
    if ch==1:
        n=int(input("Enter the number:"))
        s=0
        while n>0:
            d=n%10
            s+=d
            n=n//10
        print("Sum of digits:",s)
    elif ch==2:
        n=int(input("Enter the number:"))
        if n==1:
            print("Neither prime nor composite")
        else:
            for i in range(2,n//2):
                if n%i==0:
                    print("Not a prime")
                    break
            else:
                print("Prime")
    elif ch==3:
        strl=input("Enter a string:")
        c=0
        for i in strl:
            if i in 'aeiouAEIOU':
                c+=1
        print("Vowels:",c)
    elif ch==4:
        break
    else:
        print("Invalid Choice")




        
                    
