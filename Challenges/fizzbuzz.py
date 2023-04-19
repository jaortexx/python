my_condition = 0

while my_condition < 101:
    if my_condition % 3 != 0 and my_condition % 5 != 0:
        print(my_condition)
        my_condition += 1
    elif my_condition % 3 == 0 and my_condition % 5 != 0:
        print("Fizz")
        my_condition += 1
    elif my_condition % 3 == 0 and my_condition % 5 == 0:
        print("Fizzbuzz")
        my_condition += 1
    elif my_condition % 3 != 0 and my_condition % 5 == 0:
        print("buzz")
        my_condition += 1
    
            

        
