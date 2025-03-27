charge = 5000
age = int(input("나이: "))
if age<8:
    print("입장료: 0")
elif age<60: 
    print("입장료:", charge)
else:
    print("입장료:", charge*0.5)
