av = 5
x = int(input("How Many Chocolate you want? "))
i = 1
while i<= x:
    if x >= av:
        print("Out Of Stock")
        break
    print("choclate",i)
    i +=1
print("Bye")