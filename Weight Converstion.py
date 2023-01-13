body_weight = int(input("enter body weight = "))
weight = input("(L)bs or (K)gs: ")

if weight.upper() == "L":
    print( body_weight * 0.4, "Kgs")

else:
    print(body_weight // 0.4, "Lbs")
