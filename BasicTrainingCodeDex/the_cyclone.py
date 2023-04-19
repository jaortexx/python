height = int(input("Please, tell me your height: "))
credits = int(input("How many credits do you have?: "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride")
elif height >= 137 and credits < 10:
    print("You don't have enough to ride")
else:
    print("Invalid data")
