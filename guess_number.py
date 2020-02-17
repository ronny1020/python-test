import random
num = random.randint(1,100)
print(num)

i=0
while i < 1:
    input_num=input("Please input a number (1~100), or input Q to leave.")
    if input_num == "Q":
        break
    elif int(input_num )==num:
        print("Correct!")
        break
    elif int(input_num )>num:
        print("Too big")
    else:
        print("Too small")
