def fibonacci(x):
    if x<=0:
        return x
    else:
        return(fibonacci(x-1)+fibonacci(x-2))
n=int(input('enter number you want to show the fibonacci till ')) 
if n<=0:
    print('Enter a positive number')
else:
    print('Fibonacci series till ',n,' :')
    for i in range(n):
        print(fibonacci(i))    
