1
print "Welcome to the restaurant menu program."
2

3
menu = {}
4

5
while True:
    6
    dish_name = raw_input("Please enter the name of the dish: ")
7
dish_price = raw_input(
    "Enter the price for '%s': " % dish_name)  # optionally you can transform price from string to float
8
menu[dish_name] = dish_price
9

10
new = raw_input("Would you like to enter new dish? (yes/no) ")
11

12
if new.lower() == "no":
    13
    break
14

15
print "Menu: %s" % menu
16

17
with open("menu.txt", "w+") as menu_file:
    18
    for dish in menu:
        19
    menu_file.write("%s, %s EUR\n" % (dish, menu[dish]))
20

21
print "Goodbye!"




