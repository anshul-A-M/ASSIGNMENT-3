def factorial(n) :
    if n<2 :
        return 1
    else :
        return n * (factorial(n-1))
n=int(input("Enter a number : "))
Ans=factorial(n)
print('The factorial of', n , ' is : ', Ans)