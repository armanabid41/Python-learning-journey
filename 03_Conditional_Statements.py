#conditional type
marks=int(input("input a number:"))
if marks >= 80:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 70:
    print("Grade A-")
elif marks >= 65:
    print ("Grade B+")
elif marks >= 60:
    print ("Grade B")
elif marks >= 55:
    print ("Grade B-")
else:
   print ("Grade F")
