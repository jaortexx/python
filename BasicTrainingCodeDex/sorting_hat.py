q_1 = int(input("Do you like Dawn or Dusk?"
            "1) Dawn"
            "2) Dusk"))

q_2 = int(input("When I'm dead, I want people to remember me as: "
            "1) The good"
            "2) The great"
            "3) The wise"
            "4) The Bold"))

q_3 = int(input("Which kind of instrument most pleases your ear?"
            "1) The violin"
            "2) The trumpet"
            "3) The piano"
            "4) The drum"))

house_gryffindor = 0
house_ravenclaw = 0
house_slytherin = 0
house_hufflepuff = 0

if q_1 == 1:
    house_gryffindor += 1
    house_ravenclaw += 1
elif q_1 == 2:
    house_slytherin += 1
    house_hufflepuff += 1
else:
    print("Wrong input")

if q_2 == 1:
    house_hufflepuff += 2
elif q_2 == 2:
    house_slytherin += 2
elif q_2 == 3:
    house_ravenclaw += 2
elif q_2 == 4:
    house_gryffindor += 2
else:
    print("Wrong input")

if q_3 == 2:
    house_hufflepuff += 4
elif q_3 == 1:
    house_slytherin += 4
elif q_3 == 3:
    house_ravenclaw += 4
elif q_3 == 4:
    house_gryffindor += 4
else:
    print("Wrong input")

if house_slytherin > house_hufflepuff and house_slytherin > house_ravenclaw and house_slytherin > house_gryffindor:
    print("Slytherin!!!")
elif house_hufflepuff  > house_slytherin and house_hufflepuff > house_ravenclaw and house_hufflepuff > house_gryffindor:
    print("Hufflepuf!!!")
elif house_ravenclaw   > house_slytherin and house_ravenclaw > house_hufflepuff and house_ravenclaw > house_gryffindor:
    print("Ravenclaw!!!")
elif house_gryffindor  > house_slytherin and house_gryffindor > house_hufflepuff and house_gryffindor > house_ravenclaw:
    print("Ravenclaw!!!")
else:
    print("Wrong input")


