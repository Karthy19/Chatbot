text1=input("User:")
while(True):
    print("Bot :What mathematical operation do I want to do?")
    op=input("User:")
    print("Bot :What is the first operand?")
    n1=int(input("User:"))
    print("Bot  :What is the second operand?")
    n2=int(input("User:"))
    if(op=="add" or op=="Add" or op=="ADD" or op=="Addition" or op=="Sum" or op=="Summation"):
        print("The sum is :",(n1+n2))
    elif(op=="sub" or op=="diff" or op=="subtraction" or op=="difference"):
        print("The difference is :",(n1-n2))
    elif(op=="product" or op=="mul" or op=="multiply"):
        print("The product is :",(n1*n2))
    elif(op=="div" or op=="division"):
        print("The division is :",(n1/n2))
