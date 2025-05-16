#                      Question 1:
a=int(input("Enter a number: "))
if a%2==0:
    print("Even")
else:
    print("Odd")


#                      Question 2:
a=100
b=200
c=300
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")   
elif c>a and c>b:
    print("c is greater")


#                      Question 3:
year=int(input("Enter year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap year")  
else:
    print("Not a leap year")


#                      Question 4:
grade=int(input("Enter your grade: "))
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F")


#                      Question 5:
a=input("Enter a letter: ")
if a in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
    print("Vowel")
else:
    print("Consonant")


#                      Question 6:
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
operator=input("Enter an operator: ")
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    if b!=0:
        print(a/b)
    else:
        print("Cannot divide by zero")


#                      Question 7:
a=int(input("Enter a number: "))
if a>=1:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")


#                      Question 8:
username=input("Enter username: ")
password=input("Enter password: ")
if username=="admin" and password=="1234":
    print("Login successful")
else:
    print("Login failed")


#                      Question 9:
a=int(input("Enter the first side of triangle: "))
b=int(input("Enter the second side of triangle: "))
c=int(input("Enter the third side of triangle: "))
if a+b>c and a+c>b and b+c>a:
    print("Triangle is valid")
else:
    print("Triangle is not valid")


#                      Question 10:
w=int(input("Enter the weight(in kg):"))
h=int(input("Enter the height(in m):"))
bmi=w/(h*h)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
else:
    print("Obesity")


#                      Question 11:
p=int(input("Enter the total price: "))
if p>1000:
    discount=p*0.1
    print("Discount is 10%")
    print("Total price after discount is:", p-discount)
elif p>500 and p<=1000:
    discount=p*0.05
    print("Discount is 5%")
    print("Total price after discount is:", p-discount)
else:
    discount=0
    print("No discount")
    print("Total price is:", p)


#                      Question 12:
month=int(input("Enter the name of month: "))
if month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December":
    print("31 days")
elif month=="February":
    x=int(input("Press 1 for leap year and 0 for non-leap year: "))
    if x==1:
        print("29 days")
    else:
        print("28 days")
elif month=="April" or month=="June" or month=="September" or month=="November":
    print("30 days")
else:
    print("Invalid month")


#                      Question 13:
print("Press 1 for Check Balance\nPress 2 for Withdraw Cash\nPress 3 for Deposit Cash\nPress 4 for Exit")
balance=10000
while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Your balance is:", balance)
    elif choice==2:
        withdraw=int(input("Enter amount to withdraw: "))
        if withdraw>balance:
            print("Insufficient balance")
        else:
            balance-=withdraw
            print("Withdrawn amount is:", withdraw)
            print("Your new balance is:", balance)
    elif choice==3:
        deposit=int(input("Enter amount to deposit: "))
        balance+=deposit
        print("Deposited amount is:", deposit)
        print("Your new balance is:", balance)
    elif choice==4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")


#                      Question 14:
age=int(input("Enter your age: "))
if age>=0 and age<=1:
    print("Infant")
elif age>=2 and age<=4:
    print("Toddler")
elif age>=5 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
elif age>=60:
    print("Senior citizen")


#                      Question 15:
a=int(input("Enter a number from 1 to 7: "))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("Invalid input")