def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

number= int(input("enter the number :"))
factorial=fact(number)
print("Factorial of ", number ,"is :",factorial)