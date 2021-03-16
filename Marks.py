name = input("Hi. Please enter your name. ")
m1 = int(input("Enter your maths marks "))
m2 = int(input("Enter your Chemistry marks "))
m3 = int(input("Enter you physics marks "))
print(f"Your maths marks are {m1}")
print(f"Your chemistry marks are {m2}")
print(f"Your physics marks are {m3}")
tot = m1 + m2 + m3
avg = tot / 3
print(f"Your average is {avg}")
if avg > 90:
    print("S grade")
elif 80 < avg < 90:
    print("B Grade")
elif 70 < avg < 80:
    print("C Grade")
elif 60 < avg < 70:
    print("D grade")
else:
    print("Fail")
