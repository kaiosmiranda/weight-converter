weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").lower()
lb = 0.450


if unit == "k":
    converted = weight * lb
    print(f"Weight in Kg: {converted}")
elif unit == "l":
    converted = weight / lb
    print(f"Weight in Lbs: {converted}")
else:
    print("Invalid")