name = input("Hi. Please enter your name.")
m1 = int(input("Please enter your physics marks."))
m2 = int(input("Please enter your math marks."))
m3 = int(input("Please enter your chem marks."))
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
    
