z1 = int(raw_input("Gebe die erste Zahl ein: "))

z2 = int(raw_input("Gebe die zweite Zahl ein: "))


operator = raw_input ("Waehle eine operator (+,-,*,/): ")

if operator=="+": # khk
    wert = z1+z2
    print z1, operator, z2, "=", wert

elif operator=="-":
    wert = z1-z2
    print z1, operator, z2, "=", wert

elif operator == "*":
    wert = z1*z2
    print z1, operator, z2, "=", wert

elif operator == "/":
    wert = z1/z2
    print z1, operator, z2, "=", wert


else:
    print "Eingabe nicht verstanden. Verzeihung"


