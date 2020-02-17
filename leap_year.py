input_year = 4000
# input_year=int(input("Please input the year."))
if input_year%400 == 0:
    print("A leap year.")
elif input_year%100 == 0:
    print("Not a leap year.")
elif input_year%4 == 0:
    print("A leap year.")
else:
    print("Not a leap year.")