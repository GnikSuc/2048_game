import random

def start_game():
    matrice = []
    for i in range(4):
        matrice.append([0] * 4)
    matrice, end = add_new_number(matrice)
    return matrice, end

def game_over():
    print("Game over!")

def add_new_number(matrice):
    end = False
    # for row in matrice:
    #     if 0 not in matrice:
    #         end = True
    #         return matrice, end
            
    row = random.randint(0, 3)
    column = random.randint(0, 3)

    while(matrice[row][column] != 0):
        row = random.randint(0, 3)
        column = random.randint(0, 3)
    matrice[row][column] = 2
    return matrice, end

def show_matrice(matrice):
    for row in range(len(matrice)):
        for column in range(len(matrice[row])):
            print(matrice[row][column], end=" ")
        print(end="\n")

#def set_matrice_bool(matrice_boolean)

def move(matrice):
    while True:
        move = input("Press command (W/A/S/D): ").upper()
        if move in ['W','A','S','D']:
            break
        else:
            print("Selected key is not available! Use keys W, A, S or D...")

    matrice_boolean = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
    ]

    match move:
        # UP
        case "W":
            for row in range(len(matrice)):
                if row == 0:
                    continue
                for column in range(len(matrice[row])):
                    if (number := matrice[row][column]) > 0:
                        previous = row
                        while (previous - 1) >= 0:
                            previous -= 1
                            current = previous + 1

                            if matrice_boolean[current][column] == True:
                                matrice_boolean[previous][column] == True
                                matrice_boolean[current][column] == False

                            if (matrice[previous][column]) == 0:
                                matrice[previous][column] = number
                                matrice[current][column] = 0
                            elif (matrice[previous][column]) == number and matrice_boolean[previous][column] == False:
                                matrice[previous][column] = number * 2
                                matrice[current][column] = 0
                                matrice_boolean[previous][column] = True
                            elif (matrice[previous][column]) > number:
                                break

        # LEFT
        case "A":
            for row in range(len(matrice)):
                for column in range(len(matrice[row])):
                    if column == 0:
                        continue
                    if (number := matrice[row][column]) > 0:
                        previous = column
                        while (previous - 1) >= 0:
                            previous -= 1
                            current = previous + 1

                            if matrice_boolean[row][current] == True:
                                matrice_boolean[row][previous] == True
                                matrice_boolean[row][current] == False

                            if (matrice[row][previous]) == 0:
                                matrice[row][previous] = number
                                matrice[row][current] = 0
                            elif (matrice[row][previous]) == number and matrice_boolean[row][previous] == False:
                                matrice[row][previous] = number * 2
                                matrice[row][current] = 0
                                matrice_boolean[row][previous] = True
                            elif (matrice[row][previous]) > number:
                                break

        # DOWN
        case "S":
            for row in range(len(matrice)-1, -1, -1):
                if row == 3:
                    continue
                for column in range(len(matrice[row])):
                    if (number := matrice[row][column]) > 0:
                        following = row
                        while (following) < 3:
                            following += 1
                            current = following - 1

                            if matrice_boolean[current][column] == True:
                                matrice_boolean[following][column] == True
                                matrice_boolean[current][column] == False
                            
                            if (matrice[following][column]) == 0:
                                matrice[following][column] = number
                                matrice[current][column] = 0
                            elif (matrice[following][column]) == number and matrice_boolean[following][column] == False:
                                number = number * 2
                                matrice[following][column] = number
                                matrice[current][column] = 0
                                matrice_boolean[following][column] = True
                            elif (matrice[following][column]) > number:
                                break

        # RIGHT
        case "D":
            for row in range(len(matrice)):
                for column in range(len(matrice[row])-1, -1, -1):
                    if column == 3:
                        continue
                    if (number := matrice[row][column]) > 0:
                        following = column
                        while (following) < 3:
                            following += 1
                            current = following - 1

                            if matrice_boolean[row][current] == True:
                                matrice_boolean[row][following] == True
                                matrice_boolean[row][current] == False

                            if (matrice[row][following]) == 0:
                                matrice[row][following] = number
                                matrice[row][current] = 0
                            elif (matrice[row][following]) == number and matrice_boolean[row][following] == False:
                                matrice[row][following] = number * 2
                                matrice[row][current] = 0
                                matrice_boolean[row][following] = True
                            elif (matrice[row][following]) > number:
                                break
    return matrice


def main():
    matrice, end = start_game()
    while end == False:
        matrice, end = add_new_number(matrice)
        show_matrice(matrice)
        matrice = move(matrice) 
    game_over()

    # matrice = [
    #     [0, 2, 2, 2],
    #     [0, 0, 4, 2],
    #     [2, 2, 2, 4],
    #     [0, 0, 0, 4]
    # ]

if __name__ == "__main__":
    main()