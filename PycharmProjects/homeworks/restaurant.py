print "Our weekly menu"

menu_dict = {}


while True:
    dish = raw_input("Enter the dish: ")
    price_float = raw_input("Enter the price: ")
    menu_dict[dish] = price_float
    print "Your dish: ", menu_dict

    quest = raw_input("Do you add another dish? (yes / no) ")

    if quest == "no":
        break

print "All dishes: ", menu_dict


print "END"

menu_file = open("menu.txt", "w+")

print "Please refer to the txt"
menu_file.write("Our Weekly Menu:\n")
for dish in menu_dict:
     menu_file.write("%s, %s EUR\n" % (dish, menu_dict[dish]))

menu_file.write("\n")