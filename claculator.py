
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
    global flag,total
    if flag:
        a = int(input("Enter a number:-"))
        b = int(input("Enter b number:-"))
        print("Select Calulator options:")
        print("1. Addition")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. exit")
        option = int(input("Select option:"))

    else:
        print("Select Calulator options:")
        print("1. Addition")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        option = int(input("Select option:-"))

        a = int(input("Enter a number:-"))

    
    
    if option == 1:
        if flag == True:
            total = sum(a, b)
        else:
            total+=a
        flag = False
        print(total)
    elif option == 2:
        if flag == True:
            total = sub(a, b)
        else:
            total-=a
        flag = False
        print(total)
    elif option == 3:
        if flag == True:
            total = multiply(a, b)
        else:
            total*=a
        flag = False
        print(total)
    elif option == 4:
        if flag == True:
            total = divide(a, b)
        else:
            total /=a
        flag = False
        print(total)
    else:
        exit()
    

while True:
    header()