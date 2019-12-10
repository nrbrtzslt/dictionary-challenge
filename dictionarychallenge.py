locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

words_for_exits = {"balra": "W",
                   "jobbra": "E",
                   "előre": "N",
                   "hátra": "S"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])
    print("The available exits are: {}".format(availableExits))

    direction = input("Please enter a direction: ")
    if direction == 'Q':
        break

    if direction in words_for_exits:
        loc = exits[loc][words_for_exits[direction]]
    else:
        print("Please select a valid direction!")
