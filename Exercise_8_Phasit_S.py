'''Product code'''
mouse =1000
monitor =2500
keyboard =2500


UserNameinput = input("Username :")
PassWordinput = input("Password :")
if UserNameinput == "customer1" and PassWordinput == "shopping01":
    print("---- Welcome ---- ")
    print("----you can choose products that you would like to buy-----")
    print("1.monitor 2500 THB Per piece")
    print("2.mouse 1000 THB Per piece")
    print("3.keyboard 2500 THB Per piece")
else:
    print("Username or Password invalid")

ProductSelected=int(input("You must specify the product Number :"))
if ProductSelected == 1:
    print("1: Monitor - >Price : 2500 THB")
    Amount=int(input("Amount:"))
    print("Total Cost:", monitor*Amount)
    print("-------------------Thank for buying------------------------")
if ProductSelected == 2:
    print("2: Mouse -> Price : 1000 THB")
    Amount = int(input("Amount:"))
    print("Total Cost:", mouse * Amount)
    print("-------------------Thank for buying------------------------")
if ProductSelected == 3:
    print("3: Keyboard -> Price : 2500 THB")
    Amount = int(input("Amount:"))
    print("Total Cost:", keyboard * Amount)
    print("-------------------Thank for buying------------------------")












