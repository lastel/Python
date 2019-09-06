import random
import sys
import getpass


def uinput(text):
    return getpass.getpass(text)


def decission(decission):
    decission = decission.lower()
    decission_list = ["j", "y", "ja", "yes", None, "n", "nein", "no"]
    if not decission in decission_list or decission == None:
        return None
    return decission_list.index(decission) < decission_list.index(None)


def replace_last(string, old_pattern, new_pattern):
    start = string.rsplit(old_pattern, 1)
    return new_pattern.join(start)


def display_elements(playerName, elements):
    string = "%s, nimmst du " % playerName
    for index in range(0, len(elements)):
        element = elements[index]
        if index != 0:
            string += ", "
        string += "%s(%s)" % (element, index + 1)
    string = replace_last(string, ", ", " oder ") + "?     "
    return string


def rangedInput(message, intRange, visible = True):
    if visible:
        input_func = input
    else:
        input_func = uinput
    while 1:
        try:
            i = input_func(message)
            i = int(i)
            if i in intRange:
                return i
        except KeyboardInterrupt:
            print()
            exit()
        except ValueError:
            pass

def playerInput(name, elements):
    return rangedInput(
        display_elements(
            name,
            elements
        ),
        range(
            1,
            len(elements) + 1
        ),
        False
    )


def gewinner(p1_input, p2_input):
    if p1_input == p2_input:
        roundWinner = None
    elif(
        (p1_input == "Stein"       and (p2_input == "Schere" or p2_input == "Streichholz" or p2_input == "Feuer"      )) or
        (p1_input == "Papier"      and (p2_input == "Stein"  or p2_input == "Brunnen"     or p2_input == "Wasser"     )) or
        (p1_input == "Schere"      and (p2_input == "Papier" or p2_input == "Streichholz" or p2_input == "Wasser"     )) or
        (p1_input == "Brunnen"     and (p2_input == "Schere" or p2_input == "Stein"       or p2_input == "Wasser"     )) or
        (p1_input == "Streichholz" and (p2_input == "Papier" or p2_input == "Brunnen"     or p2_input == "Wasser"     )) or
        (p1_input == "Feuer"       and (p2_input == "Schere" or p2_input == "Papier"      or p2_input == "Streichholz")) or
        (p1_input == "Wasser"      and (p2_input == "Stein"  or p2_input == "Brunnen"     or p2_input == "Feuer"      ))
    ):
        roundWinner = 1
    else:
        roundWinner = 2

    return roundWinner



def spiel():
    nowins = 0
    p1wins = 0
    p2wins = 0
    print("Willst du mit einer Erweiterung spielen?(0 für nein)")
    print("Wenn ja, mit welcher Erweiterung? Bitte eine ganze Zahl.")
    erw = rangedInput("1 für Brunnen und Streichholz und 2 für Brunnen, Streichholz, Feuer und Wasser.     ", range(2))
    Elemente = ["Schere", "Stein", "Papier"]
    if erw >= 1:
        Elemente.append("Brunnen")
        Elemente.append("Streichholz")
    if erw == 2:
        Elemente.append("Feuer")
        Elemente.append("Wasser")
    isPlayer = None
    while isPlayer is None:
        isPlayer = decission(input("Willst du gegen einen zweiten Spieler statt gegen den Computer spielen? (j/n)     "))
    if isPlayer:
        p1name = "Spieler1"
        p2name = "Spieler2"
    else:
        p1name = "Spieler"
        p2name = "Computer"
    runden = int(input("Wie viele Runden muss man gewinnen?     "))

    while 1:
        """
        if erw == "0":
            p1_input = int(uinput("%s, Nimmst du Schere(1), Stein(2) oder Papier(3)?     " % p1name))
            if isPlayer:
                p2_input = int(uinput("Spieler2, Nimmst du Schere(1), Stein(2) oder Papier(3)?     "))
            else:
                p2_input = random.randint(1, 3)
        elif erw == "1":
            p1_input = int(uinput("%s, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4) oder Streichholz(5)?     " % p1name))
            if isPlayer:
                p2_input = int(uinput("Spieler2, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4) oder Streichholz(5)?     "))
            else:
                p2_input = random.randint(1, 5)
        else:
            p1_input = int(uinput("%s, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4), Streichholz(5), Feuer(6) oder Wasser(7)?     " % p1name))
            if isPlayer:
                p2_input = int(uinput("Spieler2, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4), Streichholz(5), Feuer(6) oder Wasser(7) ?     "))
            else:
                p2_input = random.randint(1, 7)

        """

        p1_input =     playerInput(p1name, Elemente)
        if isPlayer:
            p2_input = playerInput(p2name, Elemente)
        else:
            p2_input = random.randint(length(Elemente)) + 1


        print(Elemente, p1_input, p2_input)
        p1_input = Elemente[p1_input - 1]
        p2_input = Elemente[p2_input - 1]

        roundWinner = gewinner(p1_input, p2_input)

        if roundWinner == 1:
            roundWinnerName = p1name
            p1wins += 1
        elif roundWinner == 2:
            roundWinnerName = p2name
            p2wins += 1
        else:
            roundWinnerName = "keiner"
            nowins += 1

        print("%s hat %s gewählt und %s hat %s gewählt und desswegen hat %s die Runde gewonnen." % (p1name, p1_input, p2name, p2_input, roundWinnerName))
        print("%s hat nun %s mal gewonnen und %s %s mal. Es muss %s mal gewonnen werden."        % (p1name, p1wins,   p2name, p2wins,   runden         ))
        if p1wins >= runden:
            gameWinner = p1name
            break
        elif p2wins >= runden:
            gameWinner = p2name
            break

    print("Damit hat %s das Spiel gewonnen." % gameWinner)

if __name__ == "__main__":
    spiel()
