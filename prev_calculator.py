total =0
flag= True
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def header():
    a = int(input("Enter a number"))
    b = int(input("Enter b number"))
    print("Select Calulator options:")
    print("1. Addition")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    option = int(input("Select option:"))    
    if option == 1:
        total = sum(a, b)
        print(total)
    elif option == 2:
        total = sub(a, b)
        print(total)
    elif option == 3:
        total = multiply(a, b)
        print(total)
    elif option == 4:
        total = divide(a, b)
        print(total)
    else:
        exit()
    

while True:
    header()