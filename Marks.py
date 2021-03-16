import random
name = input("Hi. Please enter your name. ")
m1 = random.randint(20, 100)
m2 = random.randint(20, 100)
m3 = random.randint(20, 100)
print(f"Your maths marks are {m1}")
print(f"Your chemistry marks are {m2}")
print(f"Your physics marks are {m3}")
tot = m1 + m2 + m3
avg = tot / 3
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
    
