import random
import keyboard
import time

def start_game():
    print("\n*** Game 2048 ***\n")
    matrice = []
    for i in range(4):
        matrice.append([0] * 4)
    matrice = add_new_number(matrice)
    return matrice

def print_info():
    print("Use the arrows or 'W', 'A', 'S', 'D' to set the direction of the next move.\nPress 'esc' to exit anytime.\n")

def is_game_over(matrice, end):
    success = False
    zero = False

    if end == False:
        for row in matrice:
            for column in row:
                if column == 2048:
                    end = True
                    success = True
                elif column == 0:
                    zero = True
        if zero == False:
            end = True
            success = False

    lines = 7 * "\n"
    if end == True and success == False:
        print(f"{lines}Game over!\n")
    elif end == True and success == True:
        print(f"{lines}Congratulations! You successfully completed the game! :)\n")

    return end

def add_new_number(matrice):
    row = random.randint(0, 3)
    column = random.randint(0, 3)

    while(matrice[row][column] != 0):
        row = random.randint(0, 3)
        column = random.randint(0, 3)
    matrice[row][column] = 2
    return matrice

def show_matrice(matrice, moves):
    output = ""
    print(f"Moves: {moves}\n")
    
    for row in range(len(matrice)):
        output += "| "
        for column in range(len(matrice[row])):
            output += str(matrice[row][column]).center(4) + ""
        output += "|\n"

    print(output + "\033[F" * (len(matrice) + 4))
    moves += 1
    return moves    

def move(matrice, end):
    while True:
        if keyboard.is_pressed("up") or keyboard.is_pressed("w"):
            move = "UP"
        elif keyboard.is_pressed("down") or keyboard.is_pressed("s"):
            move = "DOWN"
        elif keyboard.is_pressed("left") or keyboard.is_pressed("a"):
            move = "LEFT"
        elif keyboard.is_pressed("right") or keyboard.is_pressed("d"):
            move = "RIGHT"
        elif keyboard.is_pressed("esc"):
            end = True
            break
        else:
            continue

        if end != True:
            time.sleep(0.2)
            matrice = game_logic(matrice, move)
            print("")    
            break
    return matrice, end
    

def game_logic(matrice, move):

    matrice_boolean = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
    ]

    match move:
        case "UP":
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
                                matrice_boolean[previous][column] = True
                                matrice_boolean[current][column] = False

                            if (matrice[previous][column]) == 0:
                                matrice[previous][column] = number
                                matrice[current][column] = 0
                            elif (matrice[previous][column]) == number and matrice_boolean[previous][column] == False:
                                matrice[previous][column] = number * 2
                                matrice[current][column] = 0
                                matrice_boolean[previous][column] = True
                            elif (matrice[previous][column]) > number:
                                break
        case "LEFT":
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
                                matrice_boolean[row][previous] = True
                                matrice_boolean[row][current] = False

                            if (matrice[row][previous]) == 0:
                                matrice[row][previous] = number
                                matrice[row][current] = 0
                            elif (matrice[row][previous]) == number and matrice_boolean[row][previous] == False:
                                matrice[row][previous] = number * 2
                                matrice[row][current] = 0
                                matrice_boolean[row][previous] = True
                            elif (matrice[row][previous]) > number:
                                break
        case "DOWN":
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
                                matrice_boolean[following][column] = True
                                matrice_boolean[current][column] = False
                            
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
        case "RIGHT":
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
                                matrice_boolean[row][following] = True
                                matrice_boolean[row][current] = False

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
    end = False
    moves = 0
    matrice = start_game()
    print_info()
    while end == False:
        matrice = add_new_number(matrice)
        moves = show_matrice(matrice, moves)
        matrice, end = move(matrice, end)
        end = is_game_over(matrice, end)

if __name__ == "__main__":
    main()