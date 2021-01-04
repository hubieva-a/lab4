a2 = input("a2 = ")
a1 = input("a1 = ")
b2 = input("b2 = ")
b1 = input("b1 = ")

a2 = int(a2)
a1 = int(a1)
b2 = int(b2)
b1 = int(b1)

ed = (a1 + b1)%10
dec = a2 + b2 + ((a1+b1)//10)

ed = str(ed)
dec = str(dec)

print("The final answer is: " + dec + ed)