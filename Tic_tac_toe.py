numbers = "0123456789"
coordinates_list = ["1", "2", "3"]
dictionary = {"1 1": 0, "1 2": 1, "1 3": 2, "2 1": 3, "2 2": 4, "2 3": 5, "3 1": 6, "3 2": 7, "3 3": 8}

elements = ('         ').upper()

def draw_table():
    table_elements = elements.replace("_", " ")
    print(f"""
    ---------
    | {table_elements[0]} {table_elements[1]} {table_elements[2]} |
    | {table_elements[3]} {table_elements[4]} {table_elements[5]} |
    | {table_elements[6]} {table_elements[7]} {table_elements[8]} |
    ---------
    """)

draw_table()

game_on = True
num = 1
while game_on == True:

    coordinates = input("Enter the coordinates: ")

    if coordinates[0] not in numbers or coordinates[2] not in numbers:
        print("You should enter numbers!")
    elif coordinates[0] not in coordinates_list or coordinates[2] not in coordinates_list:
        print("Coordinates should be from 1 to 3!")
    elif elements[dictionary.get(coordinates)] == "X" or elements[dictionary.get(coordinates)] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if num % 2 == 1:
            elements = list(elements)
            elements[dictionary.get(coordinates)] = "X"
            elements = "".join(elements)
            game_on = True
            draw_table()
            num += 1
            if elements[0] == elements[1] == elements[2] == "X" or elements[3] == elements[4] == elements[5] == "X" or elements[6] == elements[7] == elements[8] == "X":
                game_on = False
                print("X wins")
            elif elements[0] == elements[1] == elements[2] == "O" or elements[3] == elements[4] == elements[5] == "O" or elements[6] == elements[7] == elements[8] == "O":
                game_on = False
                print("O wins")
            elif elements[0] == elements[3] == elements[6] == "X" or elements[1] == elements[4] == elements[7] == "X" or elements[2] == elements[5] == elements[8] == "X":
                game_on = False
                print("X wins")
            elif elements[0] == elements[3] == elements[6] == "O" or elements[1] == elements[4] == elements[7] == "O" or elements[2] == elements[5] == elements[8] == "O":
                game_on = False
                print("O wins")
            elif elements[0] == elements[4] == elements[8] == "X" or elements[2] == elements[4] == elements[6] == "X":
                game_on = False
                print("X wins")
            elif elements[0] == elements[4] == elements[8] == "O" or elements[2] == elements[4] == elements[6] == "O":
                game_on = False
                print("O wins")
            elif elements[0] != " " and elements[1] != " " and elements[2] != " " and elements[3] != " " and elements[4] != " " and elements[5] != " " and elements[6] != " " and elements[7] != " " and elements[8] != " ":
                game_on = False
                print("Draw")
        elif num % 2 == 0:
            elements = list(elements)
            elements[dictionary.get(coordinates)] = "O"
            elements = "".join(elements)
            game_on = True
            draw_table()
            num += 1
            if elements[0] == elements[1] == elements[2] == "X" or elements[3] == elements[4] == elements[5] == "X" or elements[6] == elements[7] == elements[8] == "X":
                game_on = False
                print("X wins")
            elif elements[0] == elements[1] == elements[2] == "O" or elements[3] == elements[4] == elements[5] == "O" or elements[6] == elements[7] == elements[8] == "O":
                game_on = False
                print("O wins")
            elif elements[0] == elements[3] == elements[6] == "X" or elements[1] == elements[4] == elements[7] == "X" or elements[2] == elements[5] == elements[8] == "X":
                game_on = False
                print("X wins")
            elif elements[0] == elements[3] == elements[6] == "O" or elements[1] == elements[4] == elements[7] == "O" or elements[2] == elements[5] == elements[8] == "O":
                game_on = False
                print("O wins")
            elif elements[0] == elements[5] == elements[8] == "X" or elements[2] == elements[5] == elements[6] == "X":
                game_on = False
                print("X wins")
            elif elements[0] == elements[5] == elements[8] == "O" or elements[2] == elements[5] == elements[6] == "O":
                game_on = False
                print("O wins")
            elif elements[0] != " " and elements[1] != " " and elements[2] != " " and elements[3] != " " and elements[4] != " " and elements[5] != " " and elements[6] != " " and elements[7] != " " and elements[8] != " ":
                game_on = False
                print("Draw")
    

       
# draw_table()
