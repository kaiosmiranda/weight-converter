weight = float(input("Weight: "))
question = input("(K)g or (L)bs: ").lower()
lb = 0.450


if question == "k":
    total = weight * lb
    print(f"Weight in Kg: {total}")
elif question == "l":
    total = weight / lb
    print(f"Weight in Lbs: {total}")
else:
    print("Invalid")