#                      Pattern 1:                  
for i in range(1,5):
    for j in range(1,i):
        print("",end=" ")
    for j in range(1,5):
        print("*",end="")
    print("")  


#                      Pattern 2:
for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print("")


#                      Pattern 3:
for i in range(1,7):
    a="A"
    for j in range(1,i):
        print(a,end="")
        a=chr(ord(a)+1)
    print("")


#                      Pattern 4:
a="A"
for i in range(1,6):
    for j in range(1,i+1):
        print(a,end="")
    print("")
    a=chr(ord(a)+1)


#                      Pattern 5:
num=6
for i in range(1,num):
    a=chr(ord("A")+num)
    a=chr(ord(a)-(i+1))
    for j in range(1,i+1):
        print(a,end="")
        a=chr(ord(a)+1)
    print("")



#                      Pattern 6:
for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")


#                      Pattern 7:
for i in range(1,6):
    a=1
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(a,end="")
        a+=1
    print("")


#                      Pattern 8(i):
for i in range(1,6):
    a=1
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(6,i,-1):
        print(a,end="")
        a+=1
    print("")


#                      Pattern 8(ii):
for i in range(1,6):
    a="A"
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(6,i,-1):
        print(a,end="")
        a=chr(ord(a)+1)
    print("")


#                      Pattern 9:
for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,6):
        print("*",end="")
    print("")


#                      Pattern 10:
for i in range(1,6):
    a=1
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,6):
        print(a,end="")
        a+=1
    print("")


#                      Pattern 11:
for i in range(1,6):
    a="A"
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,6):
        print(a,end="")
        a=chr(ord(a)+1)
    print("")


#                      Pattern 12:
a=5
for i in range(a):
    space=' ' * (a-i-1)
    star='*' * (2*i+1)
    print(space+star)


#                      Pattern 13:
a=5
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if i==a-1 or j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print("")

#                      Pattern 14:
a=4
for i in range(a):
    space=" " * i
    star="*" * (2*(a-i)-1)
    print(space+star)


#                      Pattern 15:
for i in range(1,6):
  for j in range(1,i+1):
    print("*",end="")
  print("\n")
for i in range(6,1,-1):
  for j in range(1,i-1):
    print("*",end="")
  print("")


#                      Pattern 16:
for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")
for i in range(6,1,-1):
    for j in range(6,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")


#                      Pattern 17:
a=4
for i in range(a):
    space=' ' * (a-i-1)
    star='*' * (2*i+1)
    print(space+star)
a=3
for i in range(a):
    space=" " * i
    star="*" * (2*(a-i)-1)
    print("",space+star)


#                      Pattern 18(a):
for i in range(1,7):
    a=1
    for j in range(1,i):
        print(a,end=" ")
        a+=1
    print("")


#                      Pattern 18(b):
for i in range(1,7):
    a=1
    for j in range(7-i,1,-1):
        print(a,end=" ")
        a+=1
    print("")


#                      Pattern 18(c):
for i in range(1,6):
    a=1
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print(a,end=" ")
        else:
            print(" ",end=" ")
        a+=1
    print("")


#                      Pattern 18(d):
for i in range(1,6):
    a=0+i
    for j in range(7-i,1,-1):
        if j==7-i or j==2 or i==1:
            print(a,end=" ")
        else:
            print(" ",end=" ")
        a+=1
    print("")
