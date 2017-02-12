print "Our weekly menu"

menu_dict = {}

while True:
    dish = raw_input("Enter the dish: ")
    price = raw_input("Enter the price: ")
    print "Your dish1: " + dish + price
    quest = raw_input("Do you add another dish? (yes / no) ")

    if quest == "no":
        break
    else:
        menu_dict[dish] = False


print "All dishes: %s" % menu_dict

print "END"

print "Our Weekly Menu:"
for item in menu_dict:
    if menu_dict[dish] is True:
        print "- " + dish



menu_file = open("menu.txt", "w+")  # open the TXT file (or create a new one)

print "Our Weekly menu:"
menu_file.write("Our Weekly Menu:\n")  # write into the TXT file
for dish in menu_dict:
    if menu_dict[dish] == True:
        print "- " + dish
        menu_file.write("- " + dish + "\n")  # add task into the TXT file

menu_file.write("\n")

